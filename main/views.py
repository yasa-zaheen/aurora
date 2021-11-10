# Imports


from datetime import time
from main.models import *
from dashboard.models import *

from main.webscraper import permission
from main.product_types import *
from main.filters import *

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from asgiref.sync import sync_to_async

import json


# Views


def cart_btn_handler(request, cart):
    product = Product.objects.get(id=request.POST["cart"])

    if product in cart.products.all():
        cart.products.remove(product)
        messages.add_message(
            request, messages.ERROR, f"{product.name} has been removed from your cart.")
    else:
        cart.products.add(product)
        product_cart = ProductCart.objects.create(product=product)
        product_cart.save()
        messages.add_message(
            request, messages.SUCCESS, f"{product.name} has been added to your cart.")

    cart.save()


def watchlist_btn_handler(request, watchlist):
    product = Product.objects.get(id=request.POST["watchlist"])

    if product in watchlist.products.all():
        watchlist.products.remove(product)
        messages.add_message(
            request, messages.ERROR, f"{product.name} has been removed from your watchlist.")
    else:
        watchlist.products.add(product)
        product_watchlist = ProductsAddedToWatchlist.objects.create(
            product=product)
        product_watchlist.save()
        messages.add_message(
            request, messages.SUCCESS, f"{product.name} has been added to your watchlist.")

    watchlist.save()


def wishlist_btn_handler(request, wishlist):
    product = Product.objects.get(id=request.POST["wishlist"])

    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.add_message(
            request, messages.ERROR, f"{product.name} has been removed from your wishlist.")
    else:
        wishlist.products.add(product)
        messages.add_message(
            request, messages.SUCCESS, f"{product.name} has been added to your wishlist.")

    wishlist.save()


def index(request):
    all_categories = Category.objects.order_by('name')
    products = Product.objects.all()

    context = {
        "all_categories": all_categories,
        "products": products,
    }

    if request.user.is_authenticated:
        user = request.user
        custom_user = CustomUser.objects.get(user=user)
        cart = Cart.objects.get(user=custom_user)
        wishlist = Wishlist.objects.get(user=custom_user)
        watchlist = Watchlist.objects.get(user=custom_user)

        context["cart"] = cart
        context["wishlist"] = wishlist
        context["watchlist"] = watchlist

    if request.method == "POST":
        if request.user.is_authenticated:
            if "cart" in request.POST:
                cart_btn_handler(request, cart)

            if "wishlist" in request.POST:
                wishlist_btn_handler(request, wishlist)

            if "watchlist" in request.POST:
                watchlist_btn_handler(request, watchlist)

        else:
            return redirect(reverse("authentication:sign_in"))

    return render(request, "main/index.html", context)


def products(request):
    all_categories = Category.objects.order_by('name')
    products = Product.objects.all()

    context = {
        "all_categories": all_categories,
        "products": products,
    }

    if request.user.is_authenticated:
        user = request.user
        custom_user = CustomUser.objects.get(user=user)
        cart = Cart.objects.get(user=custom_user)
        wishlist = Wishlist.objects.get(user=custom_user)
        watchlist = Watchlist.objects.get(user=custom_user)

        context["cart"] = cart
        context["wishlist"] = wishlist
        context["watchlist"] = watchlist

    if request.method == "POST":
        if request.user.is_authenticated:
            if "cart" in request.POST:
                cart_btn_handler(request, cart)

            if "wishlist" in request.POST:
                wishlist_btn_handler(request, wishlist)

            if "watchlist" in request.POST:
                watchlist_btn_handler(request, watchlist)

        else:
            return redirect(reverse("authentication:sign_in"))

    return render(request, "main/products.html", context)


def product(request, id):
    all_categories = Category.objects.order_by('name')

    product = Product.objects.get(id=id)
    product_view = ProductView.objects.create(product=product)
    product_view.save()

    seller_products = Product.objects.filter(seller=product.seller)
    reviews = Review.objects.filter(product=product)

    context = {
        'all_categories': all_categories,
        "product": product,
        "seller_products": seller_products,
        "reviews": reviews,
    }

    if request.user.is_authenticated:
        user = request.user
        custom_user = CustomUser.objects.get(user=user)
        cart = Cart.objects.get(user=custom_user)
        wishlist = Wishlist.objects.get(user=custom_user)
        watchlist = Watchlist.objects.get(user=custom_user)

        context["cart"] = cart
        context["wishlist"] = wishlist
        context["watchlist"] = watchlist

    if request.method == "POST":
        if request.user.is_authenticated:
            if "cart" in request.POST:
                cart_btn_handler(request, cart)

            if "wishlist" in request.POST:
                wishlist_btn_handler(request, wishlist)

            if "watchlist" in request.POST:
                watchlist_btn_handler(request, watchlist)

        else:
            return redirect(reverse("authentication:sign_in"))

    return render(request, "main/product.html", context)


def category(request, id):

    category = Category.objects.get(id=id)
    sub_categories = SubCategory.objects.filter(
        category=category).order_by('name')

    all_categories = Category.objects.order_by('name')

    products = Product.objects.all()

    user = request.user
    custom_user = CustomUser.objects.get(user=user)
    cart = Cart.objects.get(user=custom_user)
    wishlist = Wishlist.objects.get(user=custom_user)
    watchlist = Watchlist.objects.get(user=custom_user)

    context = {
        "category": category,
        "sub_categories": sub_categories,
        'all_categories': all_categories,
        "products": products,
        "cart": cart,
        "wishlist": wishlist,
        "watchlist": watchlist
    }

    if request.method == "POST":
        if "cart" in request.POST:
            cart_btn_handler(request, cart)

        if "wishlist" in request.POST:
            wishlist_btn_handler(request, wishlist)

        if "watchlist" in request.POST:
            watchlist_btn_handler(request, watchlist)

    return render(request, "main/category.html", context)


def brand(request):

    context = {}
    return render(request, "main/brand.html", context)


def sub_category(request, id):

    all_categories = Category.objects.order_by('name')

    sub_category = SubCategory.objects.get(id=id)
    product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="").order_by('name')

    products = Product.objects.all()

    context = {
        "sub_category": sub_category,
        "product_types": product_types,
        'all_categories': all_categories,
        "products": products,


    }
    return render(request, "main/sub_category.html", context)


def product_type(request, id):

    all_categories = Category.objects.order_by('name')

    filter_categories = []
    filter_categorys_num = 0

    products = Product.objects.all()

    product_type = ProductType.objects.get(id=id)
    children_product_types = ProductType.objects.filter(
        parent_product_type=product_type.name, sub_category=product_type.sub_category)
    filters = Filter.objects.filter(
        product_type=product_type).order_by('filter_category', 'name')

    if len(children_product_types) != 0:
        children_product_types_exists = True
    else:
        children_product_types_exists = False

    for filter in filters:

        if filter.filter_category in filter_categories:
            pass
        else:
            filter_categories.append(filter.filter_category)
            filter_categorys_num += 1

    context = {
        "product_type": product_type,
        "children_product_types": children_product_types,
        "filters": filters,
        "filter_categories": filter_categories,
        "children_product_types_exists": children_product_types_exists,
        'all_categories': all_categories,
        "products": products,
    }
    return render(request, "main/product_type.html", context)


def seller(request):
    context = {}
    return render(request, "main/product_seller.html", context)


# permission()

# add_product_types()

# filters_for_product_type()
