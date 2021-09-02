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
    context = {}
    return render(request, "dashboard/cart.html", context)


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

            user.save()

        seller = CustomUser.objects.get(user=request.user)

        context = {
            "seller": seller
        }

        return render(request, 'dashboard/settings.html', context)
    else:
        return redirect(reverse("main:index"))


def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)
