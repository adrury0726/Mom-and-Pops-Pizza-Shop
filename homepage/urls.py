from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'cart'

urlpatterns = [
 url(r'^$', views.index, name='index'),
]
