# Imports

from django.urls import path
from . import views

# URL Configurations

app_name = "dashboard"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('dashboard', views.dashboard, name='dashboard')
]
