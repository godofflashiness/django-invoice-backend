# Generated by Django 5.0.4 on 2024-04-09 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0003_delete_razorpaytransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('order_id_long', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('method', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('woocommerce_order_number', models.IntegerField()),
                ('woocommerce_order_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('address_1', models.CharField(max_length=50)),
                ('address_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postcode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
                ('currency', models.CharField(max_length=3)),
                ('date_created', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=10)),
                ('payment_method_title', models.CharField(max_length=50)),
                ('billingAddress', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.billingaddress')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.payment')),
                ('shippingAddress', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payments.shippingaddress')),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_id', models.IntegerField()),
                ('variation_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('tax_class', models.CharField(max_length=50)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subtotal_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxes', models.TextField()),
                ('sku', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.order')),
            ],
        ),
    ]
