from django.shortcuts import render, redirect
from django.views import View

from shop.models import Layer, Berries, Topping, Shape, Decor


class IndexView(View):
    def get(self, request):
        context = {
            'layers':  Layer.objects.filter(available=True),
            'shapes': Shape.objects.filter(available=True),
            'toppings': Topping.objects.filter(available=True),
            'berries': Berries.objects.filter(available=True),
            'decors': Decor.objects.filter(available=True),
        }

        return render(request, 'index.html', context=context)

    def post(self, request):
        print(request.POST)
        return redirect('index')
