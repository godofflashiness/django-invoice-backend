# Generated by Django 5.0.4 on 2024-04-10 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_invoide_order_invoice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoide',
            new_name='Invoice',
        ),
    ]