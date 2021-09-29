# Imports


from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse

from authentication.models import *
from dashboard.models import *

from main.views import cart_btn_handler, wishlist_btn_handler, watchlist_btn_handler

# Views


def home(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        cart = Cart.objects.get(user=user)
        wishlist = Wishlist.objects.get(user=user)
        watchlist = Watchlist.objects.get(user=user)

        context = {
            "user": user,
            "cart": cart,
            "wishlist": wishlist,
            "watchlist": watchlist,
        }

        return render(request, 'dashboard/home.html', context)
    else:
        return redirect(reverse("main:index"))


def cart(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        cart = Cart.objects.get(user=user)
        wishlist = Wishlist.objects.get(user=user)
        watchlist = Watchlist.objects.get(user=user)

        context = {
            "user": user,
            "cart": cart,
            "wishlist": wishlist,
            "watchlist": watchlist,

        }

        if request.method == "POST":
            if "cart" in request.POST:
                cart_btn_handler(request, cart)

            if "wishlist" in request.POST:
                wishlist_btn_handler(request, wishlist)

            if "watchlist" in request.POST:
                watchlist_btn_handler(request, watchlist)

            if "submit-cart" in request.POST:
                order = Order.objects.create(user=user)

                for product in cart.products.all():
                    order.products.add(product)
                    cart.products.remove(product)

                order.status = "Packaging"
                order.name = request.POST["order-name"]
                order.email = request.POST["order-email"]
                order.contact = request.POST["order-contact"]
                order.address = request.POST["order-address"]
                order.zip_code = request.POST["order-zip-code"]
                order.country = request.POST["order-country"]
                order.state_province = request.POST["order-state-province"]
                order.city = request.POST["order-city"]

                order.payment_made = True

                order.save()
                cart.save()

        return render(request, "dashboard/cart.html", context)
    else:
        return redirect(reverse("main:index"))


def watchlist(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        watchlist = Watchlist.objects.get(user=user)
        watchlist.update()

        context = {
            "user": user,
            "watchlist": watchlist,
        }

        return render(request, "dashboard/watchlist.html", context)
    else:
        return redirect(reverse("main:index"))


def wishlist(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        cart = Cart.objects.get(user=user)
        wishlist = Wishlist.objects.get(user=user)
        watchlist = Watchlist.objects.get(user=user)

        context = {
            "user": user,
            "cart": cart,
            "wishlist": wishlist,
            "watchlist": watchlist,
        }

        if request.method == "POST":
            if "cart" in request.POST:
                cart_btn_handler(request, cart)

            if "wishlist" in request.POST:
                wishlist_btn_handler(request, wishlist)

            if "watchlist" in request.POST:
                watchlist_btn_handler(request, watchlist)

        return render(request, "dashboard/wishlist.html", context)
    else:
        return redirect(reverse("main:index"))


def crm(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)

        context = {
            "user": user,
        }

        return render(request, 'dashboard/crm.html', context)

    else:
        return redirect(reverse("main:index"))


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

            # **Profile Image & Cover Image**

            for i in request.FILES:
                if i == "cover-image":
                    cover_image = request.FILES["cover-image"]
                    user.cover_image = cover_image
                    messages.add_message(
                        request, messages.SUCCESS, 'Cover image changed successfully!')

                elif i == "profile-image":
                    profile_image = request.FILES["profile-image"]
                    user.profile_image = profile_image
                    messages.add_message(
                        request, messages.SUCCESS, 'Profile image changed successfully!')

            # **Personal Information**

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

            # **Password & Login**

            if request.POST['new-password'] != "":
                correct_credentials = authenticate(
                    username=user.user.username, password=request.POST['current-password'])

                if correct_credentials:
                    messages.add_message(
                        request, messages.SUCCESS, 'Passwords reset successfully!')
                    user.user.set_password(request.POST["new-password"])
                    user.user.save()
                else:
                    messages.add_message(
                        request, messages.ERROR, 'Current password is incorrect.')

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
