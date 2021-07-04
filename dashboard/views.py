# Imports

from django.shortcuts import render

# Views


def home(response):
    context = {}
    return render(response, 'dashboard/home.html', context)


def cart(response):
    context = {}
    return render(response, "dashboard/cart.html", context)


def watchlist(response):
    context = {}
    return render(response, "dashboard/watchlist.html", context)


def wishlist(response):
    context = {}
    return render(response, "dashboard/wishlist.html", context)


def crm(response):
    context = {}
    return render(response, 'dashboard/crm.html', context)


def my_products(response):
    context = {}
    return render(response, "dashboard/my_products.html", context)


def add_product(response):
    context = {}
    return render(response, "dashboard/add_product.html", context)


def revenue(response):
    context = {}
    return render(response, "dashboard/revenue.html", context)


def dashboard(response):
    context = {}
    return render(response, 'dashboard/dashboard.html', context)
