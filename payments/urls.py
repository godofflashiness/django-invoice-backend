from django.urls import path, include
from .views import payment_details, view_invoice

urlpatterns = [
    path('', payment_details, name='payment_details'),
    path('view-invoice/', view_invoice, name='view-invoice')
]
