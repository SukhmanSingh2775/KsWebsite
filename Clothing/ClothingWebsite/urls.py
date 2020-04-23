

from django.urls import include, path
from django.contrib import admin
from ClothingWebsite import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage, name='Homepage')
]
