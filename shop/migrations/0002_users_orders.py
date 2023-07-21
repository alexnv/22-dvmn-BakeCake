# Generated by Django 4.2.3 on 2023-07-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(verbose_name='Номер телефона')),
                ('address', models.TextField(verbose_name='Адрес заказчика')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Имя заказчика')),
            ],
            options={
                'verbose_name': 'Клиенты',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(verbose_name='Надпись')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий к заказу')),
                ('date_delivery', models.DateField(verbose_name='Дата доставки')),
                ('time_delivery', models.TimeField(verbose_name='Время доставки')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.users', verbose_name='Надпись')),
                ('berry', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.berries', verbose_name='Ягоды')),
                ('decor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.decor', verbose_name='Декор')),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.layer', verbose_name='Уровень')),
                ('shape', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shape', verbose_name='Форма')),
                ('topping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.topping', verbose_name='топпинг')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]