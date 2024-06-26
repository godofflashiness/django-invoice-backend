# Generated by Django 5.0.4 on 2024-04-10 04:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=50)),
                ('invoice_date', models.DateTimeField()),
                ('invoice_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='invoice',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.invoide'),
        ),
    ]
