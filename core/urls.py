
from django.contrib import admin
from django.urls import include, path
from .views import login

urlpatterns = [
    path('',login,name='login')
]
