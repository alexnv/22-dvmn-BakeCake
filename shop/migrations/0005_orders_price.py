# Generated by Django 4.2.3 on 2023-07-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_customers_utmcheckin_remove_orders_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
