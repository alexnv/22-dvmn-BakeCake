# Generated by Django 4.2.3 on 2023-07-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='delivery_address',
            field=models.TextField(blank=True, verbose_name='Адрес доставки'),
        ),
        migrations.AddField(
            model_name='orders',
            name='delivery_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий для курьера'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='word',
            field=models.TextField(verbose_name='Надпись на торте'),
        ),
    ]