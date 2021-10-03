# Imports

from django.urls import path
from . import views

# URL Configurations

app_name = "dashboard"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('watchlist/', views.watchlist, name="watchlist"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path('crm/', views.crm, name="crm"),
    path('crm/order/<int:id>', views.order, name="order"),
    path("my_products/", views.my_products, name="my_products"),
    path("my_products/edit_product/<int:id>",
         views.edit_product, name="edit_product"),
    path("add_product/", views.add_product, name="add_product"),
    path('revenue/', views.revenue, name="revenue"),
    path('settings/', views.settings, name="settings")
]
