# Imports

from django.urls import path
from . import views

# URL Configurations

app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("product/", views.product, name="product"),
    path("category/<int:id>", views.category, name="category"),
    path("brand/", views.brand, name="brand"),
    path("sub_category/<int:id>", views.sub_category, name="sub_category"),
    path("product_type/<int:id>", views.product_type, name="product_type"),
    path("seller/", views.seller, name="seller"),
]
