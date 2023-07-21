from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('lk/', login_required(login_url='index')(IndexView.as_view()), name='lk'),
]
