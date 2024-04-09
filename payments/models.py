from django.db import models

class Payment(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    order_id_long = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    method = models.CharField(max_length=10)
    description = models.TextField()
    woocommerce_order_number = models.IntegerField()
    woocommerce_order_id = models.IntegerField()

class BillingAddress(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True, blank=True)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True, blank=True)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)  

class Order(models.Model):
    id = models.CharField(max_length=50, primary_key=True)

    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    billingAddress = models.OneToOneField(BillingAddress, on_delete=models.CASCADE)
    shippingAddress = models.OneToOneField(ShippingAddress, on_delete=models.CASCADE)

    status = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10)
    payment_method_title = models.CharField(max_length=50)

class LineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    product_id = models.IntegerField()
    variation_id = models.IntegerField()
    quantity = models.IntegerField()
    tax_class = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.TextField()
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)