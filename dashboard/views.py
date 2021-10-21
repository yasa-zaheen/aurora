# Imports


from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, reverse

from authentication.models import *
from dashboard.models import *
from main.models import Category, Filter, ProductType, SubCategory

from main.views import cart_btn_handler, category, product, product_type, sub_category, wishlist_btn_handler, watchlist_btn_handler

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
        return redirect(reverse("dashboard:set_sub_category", kwargs={"id": 8}))


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
                cart.create_order(request)

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


def order(request, id):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        order = Order.objects.get(id=id)

        total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
            request.user)

        if request.method == "POST":
            order.status = request.POST['order-status']

        order.save()

        context = {
            "user": user,
            "order": order,
            "total_product_price": total_product_price,
            "total_shipping": total_shipping,
            "total_revenue": total_revenue,
        }

        return render(request, 'dashboard/order.html', context)

    else:
        return redirect(reverse("main:index"))


def my_products(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        products = Product.objects.filter(seller=user)

        context = {
            "products": products
        }

        return render(request, "dashboard/my_products.html", context)

    else:
        return redirect(reverse("main:index"))


def edit_product(request, id):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)
        product = Product.objects.get(id=id)

        if request.method == "POST":
            product.edit_product(request)

        context = {
            "product": product
        }

        return render(request, "dashboard/edit_product.html", context)

    else:
        return redirect(reverse("main:index"))


def add_product(request):

    if request.user.is_authenticated:
        user = CustomUser.objects.get(user=request.user)

        if request.method == "POST":
            product = user.add_product(request)
            return redirect(reverse("dashboard:set_category", kwargs={"id": product.id}))

        context = {}

        return render(request, "dashboard/add_product.html", context)

    else:
        return redirect(reverse("main:index"))


def set_category(request, id):

    if request.user.is_authenticated:

        categories = Category.objects.all()
        product = Product.objects.get(id=id)

        if product.category == None:
            if request.method == "POST":
                category = Category.objects.get(id=request.POST["category"])
                product.category = category
                product.save()
                return redirect(reverse("dashboard:set_sub_category", kwargs={"id": product.id}))

        else:
            return redirect(reverse("dashboard:home"))

        context = {
            "categories": categories
        }

        return render(request, "dashboard/set_category.html", context)

    else:
        return redirect(reverse("main:index"))


def set_sub_category(request, id):

    if request.user.is_authenticated:

        product = Product.objects.get(id=id)
        sub_categories = SubCategory.objects.filter(category=product.category)

        if product.sub_category == None:
            if request.method == "POST":
                sub_category = SubCategory.objects.get(
                    id=request.POST["sub-category"])
                product.sub_category = sub_category
                product.save()
                return redirect(reverse("dashboard:set_product_type", kwargs={"id": product.id}))

        else:
            return redirect(reverse("dashboard:home"))

        context = {
            "sub_categories": sub_categories
        }

        return render(request, "dashboard/set_sub_category.html", context)

    else:
        return redirect(reverse("main:index"))


def set_product_type(request, id):

    if request.user.is_authenticated:

        product = Product.objects.get(id=id)
        product_types = ProductType.objects.filter(
            sub_category=product.sub_category)

        if product.product_type == None:
            if request.method == "POST":
                product_type = ProductType.objects.get(
                    id=request.POST["product-type"])
                product.product_type = product_type
                product.save()
                return redirect(reverse("dashboard:set_filters", kwargs={"id": product.id}))

        else:
            return redirect(reverse("dashboard:home"))

        context = {
            "product_types": product_types
        }

        return render(request, "dashboard/set_product_type.html", context)

    else:
        return redirect(reverse("main:index"))


def set_filters(request, id):

    if request.user.is_authenticated:

        product = Product.objects.get(id=id)
        filters = Filter.objects.filter(
            product_type=product.product_type)
        filter_categories = []

        for filter in filters:
            if filter.filter_category not in filter_categories:
                filter_categories.append(filter.filter_category)

        if request.method == "POST":
            for i in request.POST:
                if i != "csrfmiddlewaretoken":
                    filter = Filter.objects.get(id=request.POST[i])
                    product.filters.add(filter)
                    product.save()
                    return redirect(reverse("main:product"), kwargs={"id": product.id})

        context = {
            "filters": filters,
            "filter_categories": filter_categories
        }

        return render(request, "dashboard/set_filters.html", context)

    else:
        return redirect(reverse("main:index"))


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
