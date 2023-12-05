from django.urls import path
from django.contrib import admin
from car_rental_app import admin
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('signup/', views.signup_view, name='signup'),
    # Other app-specific URLs...
]


