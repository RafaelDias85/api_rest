from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_usuarios, name='get_all_users'),
    path('usuario/<str:nick>', views.get_by_nick)

     
]
