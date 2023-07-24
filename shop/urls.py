from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('payment', views.payment, name='payment'),
    path('lk/', login_required(login_url='index')(views.lk), name='lk'),
]
