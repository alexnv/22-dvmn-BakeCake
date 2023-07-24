from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from bakecake import settings
from shop.models import Layer, Berries, Topping, Shape, Decor, UtmCheckin, Customers, Orders


def index(request):
    context = {
        'layers': Layer.objects.filter(available=True),
        'shapes': Shape.objects.filter(available=True),
        'toppings': Topping.objects.filter(available=True),
        'berries': Berries.objects.filter(available=True),
        'decors': Decor.objects.filter(available=True),
    }

    return render(request, 'index.html', context=context)


@require_http_methods(['POST'])
def login_page(request):
    payload = dict(request.POST.items())
    phone = payload['REG']
    user = authenticate(username=phone, password='1234')
    if not user:
        user = User.objects.create_user(
            username=phone,
            password='1234'
        )

    login(request, user)

    client, created = Customers.objects.get_or_create(
        user=user,
        phone=phone,
        defaults={
            'address': '',
        },
    )

    return redirect('lk')

    # response = render(request, 'lk.html', get_context(client))
    # response.set_cookie('phone', str(phone))
    # return response


def get_context(client):
    serialised_orders = []
    for order in client.orders.all():
        serialised_orders.append({
            'status': order.status,
            'number': order.id,
            'status_display': order.get_status_display(),
            'layers': order.layer,
            'shape': order.shape,
            'topping': order.topping,
            'berries': order.berry,
            'decor': order.decor,
            'text': order.word,
            'price': order.price,
            'delivery_date': order.date_delivery,
            'time_delivery': order.time_delivery,

        })

    return {
        'is_debug': settings.DEBUG,
        'user': {
            'phone': str(client.phone),
            'name': client.user.username,
            'email': client.user.email,
            'address': client.address,
            'client_label': '' if (not client.user.username) else client.user.username[:1],
        },
        'orders': serialised_orders,
    }


def logout_page(request):
    logout(request)
    response = render(request, 'index.html')
    response.delete_cookie('phone')
    return response


@require_http_methods(['POST'])
def payment(request):
    pass


def lk(request):
    user = request.user
    client = user.customer.get()
    context = get_context(client)
    response = render(request, 'lk.html', context)
    response.set_cookie('phone', str(client.phone))
    return response


@require_http_methods(['POST'])
def makeorder(request):
    if request.user.is_authenticated:
        client = Customers.objects.get(user=request.user)
        user = client.user
    else:
        phone = request.POST.get('PHONE')
        user = User.objects.create_user(
            username=phone,
            password='1234'
        )
        client, created = Customers.objects.get_or_create(
            user=user,
            phone=phone,
            defaults={
                'address': '',
            },
        )

        login(request, user)
    name = request.POST.get('NAME')
    if name:
        user.name = name
        user.save()
    d_date = request.POST.get('DATE', '1970-01-01')
    d_time = request.POST.get('TIME', '00:00')

    price = int(request.POST.get('COST', 10000))

    order = Orders(
        customer=client,
        layer_id=request.POST.get('LEVELS'),
        shape_id=request.POST.get('FORM'),
        topping_id=request.POST.get('TOPPING'),
        berry_id=request.POST.get('BERRIES', '1'),
        decor_id=request.POST.get('DECOR', '1'),
        word=request.POST.get('WORDS', '1'),
        comment=request.POST.get('COMMENTS', ''),
        price=price,
        delivery_address=request.POST.get('ADDRESS'),
        delivery_comment=request.POST.get('DELIVCOMMENTS'),
        date_delivery=datetime.strptime(f"{d_date}", "%Y-%m-%d"),
        time_delivery=datetime.strptime(f"{d_time}", "%H:%M")
    )
    order.save()
    return redirect('lk')

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
