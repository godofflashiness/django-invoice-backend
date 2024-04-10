# Generated by Django 5.0.4 on 2024-04-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_rename_invoice_flag_invoice_invoice_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cgst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='igst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='sgst',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
