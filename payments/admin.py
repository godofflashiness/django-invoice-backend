from django.contrib import admin

from .models import Payment, BillingAddress, ShippingAddress, Order, LineItem

admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(LineItem)