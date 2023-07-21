from django.contrib import admin

from .models import Layer, Shape, Topping, Berries, Decor, Users, Orders


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    search_fields = ('num_layers', 'price')
    readonly_fields = []
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
    readonly_fields = []
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Berries)
class BerriesAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = []
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    readonly_fields = []
    list_display = [
        'name',
        'price',
        'available',
    ]


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone')
    list_display = [
        'name',
        'phone',
        'address',
    ]
    raw_id_fields = ['name']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    search_fields = ['address']
    list_display = [
        'address',
    ]
    raw_id_fields = ['address']
