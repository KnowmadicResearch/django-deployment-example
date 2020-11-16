from django.contrib import admin
from .views import News
from django.urls import path

urlpatterns = [
    path('', News, name= 'News'),
]