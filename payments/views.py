from typing import Dict, List, Optional, Union
import base64
import aiohttp
import asyncio
import json
import os
from asgiref.sync import sync_to_async


from django.conf import settings
from django.http import JsonResponse
from django.http import HttpRequest

from django.shortcuts import render
import razorpay
import requests

from .models import Payment, BillingAddress, ShippingAddress, Order, LineItem

def get_woo_order_id(notes: Union[Dict, List]) -> Optional[str]:
    """
    Extracts the WooCommerce order number from the payment notes.
    """
    if isinstance(notes, dict):
        return notes.get('woocommerce_order_number')
    elif isinstance(notes, list):
        for note in notes:
            if isinstance(note, dict) and 'woocommerce_order_number' in note:
                return note['woocommerce_order_number']
    return None

def get_woo_api_headers() -> Dict[str, str]:
    """
    Returns the headers for the WooCommerce API request.
    """
    auth_string = f'{settings.WOOCOMMERCE_API_KEY}:{settings.WOOCOMMERCE_API_SECRET}'
    encoded_auth_string = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
    headers = {'Authorization': f'Basic {encoded_auth_string}'}
    return headers

async def fetch_order_data(session, woo_order_id, headers):
    woo_api_url = f'https://www.paroshiltex.com/wp-json/wc/v3/orders/{woo_order_id}'
    async with session.get(woo_api_url, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            print("Error fetching WooCommerce order details.")
            return None

def populate_database_from_json():
    json_file = 'payments_data.json'
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            try:
                payments = json.load(f)
            except json.decoder.JSONDecodeError:
                print("Error decoding JSON from file.")
                return

            for payment_order in payments:
                payment = payment_order['payment']
                order_data = payment_order['order']

                if not Payment.objects.filter(id=payment['id']).exists():
                    notes = payment.get('notes', {})
                    woocommerce_order_number = int(notes.get('woocommerce_order_number', 0))
                    woocommerce_order_id = int(notes.get('woocommerce_order_id', 0))
                    payment_model = Payment.objects.create(
                        id=payment['id'],
                        order_id_long=payment['order_id'],
                        status=payment['status'],
                        method=payment['method'],
                        description=payment['description'],
                        woocommerce_order_number=woocommerce_order_number,
                        woocommerce_order_id=woocommerce_order_id
                    )

                    billing_address_model = BillingAddress.objects.create(
                        first_name=order_data['billing']['first_name'],
                        last_name=order_data['billing']['last_name'],
                        company=order_data['billing']['company'],
                        address_1=order_data['billing']['address_1'],
                        address_2=order_data['billing']['address_2'],
                        city=order_data['billing']['city'],
                        state=order_data['billing']['state'],
                        postcode=order_data['billing']['postcode'],
                        country=order_data['billing']['country'],
                        phone=order_data['billing']['phone']
                    )

                    shipping_address_model = ShippingAddress.objects.create(
                        first_name=order_data['shipping']['first_name'],
                        last_name=order_data['shipping']['last_name'],
                        company=order_data['shipping']['company'],
                        address_1=order_data['shipping']['address_1'],
                        address_2=order_data['shipping']['address_2'],
                        city=order_data['shipping']['city'],
                        state=order_data['shipping']['state'],
                        postcode=order_data['shipping']['postcode'],
                        country=order_data['shipping']['country'],
                        phone=order_data['shipping']['phone']
                    )


                    order_model = Order.objects.create(
                        id=order_data['id'],
                        status=order_data['status'],
                        currency=order_data['currency'],
                        date_created=order_data['date_created'],
                        total=float(order_data['total']),
                        total_tax=float(order_data['total_tax']),
                        payment_method=order_data['payment_method'],
                        payment_method_title=order_data['payment_method_title'],
                        payment=payment_model,
                        billingAddress=billing_address_model,
                        shippingAddress=shipping_address_model,
                    )

                    for line_item in order_data['line_items']:
                        LineItem.objects.create(
                            order=order_model,
                            id=line_item['id'],
                            name=line_item['name'],
                            product_id=int(line_item['product_id']),
                            variation_id=line_item['variation_id'],
                            quantity=int(line_item['quantity']),
                            tax_class=line_item['tax_class'],
                            subtotal=float(line_item['subtotal']),
                            subtotal_tax=float(line_item['subtotal_tax']),
                            total=float(line_item['total']),
                            total_tax=float(line_item['total_tax']),
                            sku=line_item['sku'],
                            price=float(line_item['price']),
                    )


async def payment_details(request: HttpRequest) -> JsonResponse:
    """
    Retrieves payment and order details from a payment gateway and a WooCommerce API.
    Returns the data as a JSON response.
    """
    json_file = 'payments_data.json'
    stored_payments = []
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            try:
                stored_payments = json.load(f)
            except json.decoder.JSONDecodeError:
                stored_payments = []

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payments_data = client.payment.all()
    payments_data = payments_data['items'][:]

    payments = []
    headers = get_woo_api_headers()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for payment in payments_data:
            if isinstance(payment, dict):
                order_id = payment.get('order_id')
                order_data = None
                notes = payment.get('notes', [])
                woo_order_id = get_woo_order_id(notes)
                print(f"woo_order_id: {woo_order_id}") 
                if woo_order_id:
                    task = fetch_order_data(session, woo_order_id, headers)
                    tasks.append(task)

        order_data_list = await asyncio.gather(*tasks)

        for payment, order_data in zip(payments_data, order_data_list):
            payment_order = {
                'payment': payment,
                'order': order_data
            }
            if payment_order not in stored_payments:
                payments.append(payment_order)

    with open(json_file, 'w') as f:
        json.dump(payments, f)

    await sync_to_async(populate_database_from_json)()

    context = {'payments': payments}
    return JsonResponse(context)


def view_invoice(request):
    return render(request, 'payments/invoice.html', {})

