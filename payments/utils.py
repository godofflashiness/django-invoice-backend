from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Invoice
from datetime import datetime

def generate_invoice_number():
    date_part = datetime.now().strftime('%Y%m%d')
    if not hasattr(generate_invoice_number, "counter"):
        generate_invoice_number.counter = 1
    else:
        generate_invoice_number.counter += 1
    new_number = str(generate_invoice_number.counter).zfill(4)
    return date_part + new_number

def calculate_line_item_taxes(line_items, shipping_state):
    for item in line_items:
        total_product_amount = item.total

        if shipping_state == 'WB':
            if total_product_amount < 1000:
                sgst = total_product_amount * 0.025
                cgst = total_product_amount * 0.025
            else:
                sgst = total_product_amount * 0.06
                cgst = total_product_amount * 0.06
            item.price = item.price - ( sgst + cgst )
            item.sgst = sgst
            item.cgst = cgst
            item.igst = None  # IGST is None for intra-state
        

        else:  # Other states
            if total_product_amount < 1000:
                igst = total_product_amount * 0.05
            else:
                igst = total_product_amount * 0.12
            item.price = item.price - igst
            item.sgst = None  # SGST is None for inter-state
            item.cgst = None  # CGST is None for inter-state
            item.igst = igst

        item.total_tax = item.sgst + item.cgst if item.sgst and item.cgst else item.igst
        item.save()  # Update the line item