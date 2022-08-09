from django.contrib import admin
from django.urls import path, include
from produto.views import home

urlpatterns = [
    path('', home.as_view(), name='home'),
]