# Imports

from django.shortcuts import render, redirect, reverse
from authentication.models import *
from dashboard.models import *

# Views


def home(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        cart = Cart.objects.get(user=user)

        context = {
            "user": user,
            "cart": cart,
        }

        return render(request, 'dashboard/home.html', context)
    else:
        return redirect(reverse("main:index"))


def cart(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        cart = Cart.objects.get(user=user)

        context = {
            "user": user,
            "cart": cart,
        }

        return render(request, "dashboard/cart.html", context)
    else:
        return redirect(reverse("main:index"))


def watchlist(request):
    context = {}
    return render(request, "dashboard/watchlist.html", context)


def wishlist(request):
    context = {}
    return render(request, "dashboard/wishlist.html", context)


def crm(request):
    context = {}
    return render(request, 'dashboard/crm.html', context)


def my_products(request):
    context = {}
    return render(request, "dashboard/my_products.html", context)


def add_product(request):
    context = {}
    return render(request, "dashboard/add_product.html", context)


def revenue(request):
    context = {}
    return render(request, "dashboard/revenue.html", context)


def settings(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            user = CustomUser.objects.get(user=request.user)

            for i in request.FILES:
                if i == "cover-image":
                    cover_image = request.FILES["cover-image"]
                    user.cover_image = cover_image

                elif i == "profile-image":
                    profile_image = request.FILES["profile-image"]
                    user.profile_image = profile_image

            full_name = request.POST["full-name"]
            contact = request.POST["contact"]
            address = request.POST["address"]
            zip_code = request.POST["zip-code"]
            country = request.POST["country"]
            state_province = request.POST["state-province"]
            city = request.POST["city"]

            user.full_name = full_name
            user.contact = contact
            user.address = address
            user.zip_code = zip_code
            user.country = country
            user.state_province = state_province
            user.city = city

            user.save()

        user = CustomUser.objects.get(user=request.user)

        context = {
            "user": user
        }

        return render(request, 'dashboard/settings.html', context)
    else:
        return redirect(reverse("main:index"))


def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
