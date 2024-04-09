# Generated by Django 5.0.4 on 2024-04-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='razorpaytransaction',
            name='contact',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='error_code',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='error_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='method',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='notes',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='razorpaytransaction',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='currency',
            field=models.CharField(default='INR', max_length=3),
        ),
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='razorpay_order_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='razorpay_payment_id',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='razorpaytransaction',
            name='status',
            field=models.CharField(default='', max_length=255),
        ),
    ]
