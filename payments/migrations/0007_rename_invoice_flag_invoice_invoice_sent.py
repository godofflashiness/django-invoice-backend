# Generated by Django 5.0.4 on 2024-04-10 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_rename_invoide_invoice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_flag',
            new_name='invoice_sent',
        ),
    ]