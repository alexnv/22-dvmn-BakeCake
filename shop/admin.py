from django.contrib import admin

from .models import Layer, Shape, Topping, Berries, Decor, Customers, Orders, UtmCheckin


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    search_fields = ('num_layers', 'price')
    readonly_fields = ['price']
    list_display = [
        'num_layers',
        'price',
        'available',
    ]


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = ['price']
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = ['price']
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Berries)
class BerriesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = ['price']
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = ['price']
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    search_fields = ('user', 'phone')
    list_display = [
        'user',
        'phone',
        'address',
    ]
    raw_id_fields = ['user']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    search_fields = ['customer']
    list_display = [
        'customer',
    ]
    raw_id_fields = ['customer']


@admin.register(UtmCheckin)
class UtmCheckinAdmin(admin.ModelAdmin):
    search_fields = ('utm_source', 'check_in_date')
    list_display = [
        'utm_source',
        'check_in_date',
        'utm_term',
    ]