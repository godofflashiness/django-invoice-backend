from django.urls import path, include
from .views import payment_details, view_invoice, payments_list_view, payment_details_view_json, payment_details_view_html

urlpatterns = [
    path('', payment_details, name='payment_details'),
    path('view-invoice/', view_invoice, name='view-invoice'),
    path('payments_list/', payments_list_view, name='payments_list'),
    path('payment_details/<str:payment_id>/json/', payment_details_view_json, name='payment_details_json'),
    path('payment_details_html/<str:payment_id>/html/', payment_details_view_html, name='payment_details_html'),
]
