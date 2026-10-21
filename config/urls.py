
from turtle import home

from django.contrib import admin
from django.contrib.admin import views
from django.urls import path
from ALPHA.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')
]
