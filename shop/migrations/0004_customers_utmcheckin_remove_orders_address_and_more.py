# Generated by Django 4.2.3 on 2023-07-24 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(verbose_name='Номер телефона')),
                ('address', models.TextField(verbose_name='Адрес заказчика')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Имя заказчика')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='UtmCheckin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateTimeField(auto_now=True, verbose_name='Время захода')),
                ('utm_source', models.CharField(max_length=100, verbose_name='Источник UTM')),
                ('utm_medium', models.CharField(max_length=10, verbose_name='Тип траффика')),
                ('utm_campaign', models.CharField(max_length=100, verbose_name='Название компании')),
                ('utm_content', models.CharField(max_length=250, verbose_name='Идентификатор объявления')),
                ('utm_term', models.CharField(max_length=100, verbose_name='Ключевое слово')),
            ],
            options={
                'verbose_name': 'UTM метка',
                'verbose_name_plural': 'UTM метки',
            },
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.customers', verbose_name='Клиент'),
        ),
    ]