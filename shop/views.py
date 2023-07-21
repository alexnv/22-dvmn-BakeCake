from audioop import reverse
from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View

from shop.models import Layer, Berries, Topping, Shape, Decor, Customers, Orders, UtmCheckin


class IndexView(View):
    def get(self, request):
        context = {
            'layers':  Layer.objects.filter(available=True),
            'shapes': Shape.objects.filter(available=True),
            'toppings': Topping.objects.filter(available=True),
            'berries': Berries.objects.filter(available=True),
            'decors': Decor.objects.filter(available=True),
            'users': Customers.objects.filter(available=True),
            'orders': Orders.objects.filter(available=True),
            'UTM-label': UtmCheckin.objects.filter(available=True),
        }

        return render(request, 'index.html', context=context)

    def post(self, request):
        print(request.POST)
        return redirect('index')


def check_utm(request):

    get_referer = request.GET.get('utm_source')

    if not get_referer:
        return reverse('index')

    UtmCheckin.objects.create(
        check_in_date=datetime.datetime.now(),
        utm_source=request.GET.get('utm_source'),
        utm_medium=request.GET.get('utm_medium'),
        utm_campaign=request.GET.get('utm_campaign'),
        utm_content=request.GET.get('utm_content'),
        utm_term=request.GET.get('utm_term')
    )

    return reverse('index')