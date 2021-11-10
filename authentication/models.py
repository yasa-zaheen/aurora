# Imports
from datetime import date
from django.db import models
from django.apps import apps
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(default="",  max_length=255)
    profile_image = models.ImageField(
        upload_to="profile_images", default="profile_images/user.png")
    cover_image = models.ImageField(
        upload_to="cover_images", default="cover_images/cover.jpg")
    huid = models.CharField(default="",  max_length=32)
    contact = models.CharField(default="",  max_length=255)
    is_verified = models.BooleanField(default=False)

    address = models.CharField(default="",  max_length=255)
    zip_code = models.CharField(default="",  max_length=32)
    country = models.CharField(default="",  max_length=32)
    state_province = models.CharField(default="",  max_length=32)
    city = models.CharField(default="",  max_length=32)

    account_type = models.CharField(max_length=255, choices=[
        ("New Seller", "New Seller"),
        ("Top Rated Seller", "Top Rated Seller"),
        ("Verified Seller", "Verified Seller")
    ], default="New Seller")

    communication = models.FloatField(null=True)
    shipping = models.FloatField(null=True)
    returns = models.FloatField(null=True)

    def __str__(self):
        return self.user.username

    def get_seller_orders(self):

        product_object = apps.get_model("main", "Product")
        order_object = apps.get_model("dashboard", "Order")

        products = product_object.objects.filter(seller=self)

        arr = []

        for product in products:
            set = order_object.objects.filter(products=product)
            if len(set) != 0:
                if set[0] not in arr:
                    arr.append(set[0])

        return arr

    def add_product(self, request):

        product_object = apps.get_model("main", "Product")

        product = product_object.objects.create(
            name=request.POST['name'],
            seller=self,

            price=request.POST['price'],
            stock=request.POST['stock'],

            image_1=request.FILES["image-1"],
            image_2=request.FILES["image-2"],
            image_3=request.FILES["image-3"],
            image_4=request.FILES["image-4"],

            condition=request.POST["condition"],
            shipping=request.POST["shipping"],
            returns=request.POST["returns"],

            product_does_not_ship_to=request.POST["product-does-not-ship-to"],
            shipping_price=request.POST["shipping-price"],
            product_location=request.POST["product-location"],

            payments_paypal=True
            if "paypal" in request.POST else False,
            payments_master_card=True
            if "mastercard" in request.POST else False,
            payments_visa=True
            if "visa" in request.POST else False,

            features=request.POST["features"]

        )

        product.save()

        return product

    def get_todays(self):

        orders = self.get_seller_orders()
        todays_orders = []

        revenue = 0
        sold = 0

        for order in orders:

            if order.time_of_order.astimezone(tz=None).date() == timezone.localdate():
                todays_orders.append(order)

        for order in todays_orders:
            total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
                self.user)

            sold += order.products.all().count()
            revenue += total_revenue

        return revenue, sold, todays_orders

    def get_yesterdays(self):

        orders = self.get_seller_orders()
        yesterdays_orders = []

        revenue = 0
        sold = 0

        for order in orders:
            date_time_delta = order.time_of_order.astimezone(
                tz=None).day - timezone.now().astimezone(tz=None).day

            if order.time_of_order.astimezone(tz=None).date() != timezone.localdate():
                if date_time_delta == -1:
                    yesterdays_orders.append(order)

        for order in yesterdays_orders:
            total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
                self.user)

            sold += order.products.all().count()

            revenue += total_revenue

        return revenue, sold, yesterdays_orders

    def get_lastweeks(self):

        orders = self.get_seller_orders()
        lastweeks_orders = []

        revenue = 0
        sold = 0

        for order in orders:
            date_time_delta = order.time_of_order - timezone.now()

            if date_time_delta.days <= 0 and date_time_delta.days >= -7:
                lastweeks_orders.append(order)

        for order in lastweeks_orders:
            total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
                self.user)

            sold += order.products.all().count()

            revenue += total_revenue

        return revenue, sold, lastweeks_orders

    def get_last28(self):

        orders = self.get_seller_orders()
        last28_orders = []

        revenue = 0
        sold = 0

        for order in orders:
            date_time_delta = order.time_of_order - timezone.now()

            if date_time_delta.days <= 0 and date_time_delta.days >= -28:
                last28_orders.append(order)

        for order in last28_orders:
            total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
                self.user)

            sold += order.products.all().count()

            revenue += total_revenue

        return revenue, sold, last28_orders

    def get_total_revenuesales(self):

        orders = self.get_seller_orders()

        revenue = 0
        sold = 0

        for order in orders:
            total_product_price, total_shipping, total_revenue = order.get_seller_revenue(
                self.user)

            revenue += total_revenue
            sold += order.products.all().count()

        return revenue, sold

    def get_total_views(self):
        product_object = apps.get_model("main", "Product")
        product_view_object = apps.get_model("main", "ProductView")

        total_views = 0
        products = product_object.objects.filter(seller=self)

        for product in products:
            total_views += product_view_object.objects.filter(
                product=product).count()

        product_views = []
        for product in products:
            product_views += product_view_object.objects.filter(
                product=product)

        lastweeks_views = []
        for product_view in product_views:
            delta = product_view.time.astimezone(
                tz=None).day - timezone.now().astimezone(tz=None).day
            if delta >= -7:
                lastweeks_views.append(product_view)

        return total_views, lastweeks_views

    def get_total_atc(self):
        product_object = apps.get_model("main", "Product")
        product_cart_object = apps.get_model("main", "ProductCart")

        total_atc = 0
        products = product_object.objects.filter(seller=self)

        for product in products:
            total_atc += product_cart_object.objects.filter(
                product=product).count()

        product_carts = []
        for product in products:
            product_carts += product_cart_object.objects.filter(
                product=product)

        lastweeks_carts = []
        for product_cart in product_carts:
            delta = product_cart.time.astimezone(
                tz=None).day - timezone.now().astimezone(tz=None).day
            if delta >= -7:
                lastweeks_carts.append(product_cart)

        return total_atc, lastweeks_carts

    def get_total_atwa(self):
        product_object = apps.get_model("main", "Product")
        product_watchlist_object = apps.get_model(
            "main", "ProductsAddedToWatchlist")

        total_atwa = 0
        products = product_object.objects.filter(seller=self)

        for product in products:
            total_atwa += product_watchlist_object.objects.filter(
                product=product).count()

        product_watchlists = []
        for product in products:
            product_watchlists += product_watchlist_object.objects.filter(
                product=product)

        lastweeks_watchlists = []
        for product_watchlist in product_watchlists:
            delta = product_watchlist.time.astimezone(
                tz=None).day - timezone.now().astimezone(tz=None).day
            if delta >= -7:
                lastweeks_watchlists.append(product_watchlist)

        return total_atwa, lastweeks_watchlists

    def get_total_atwi(self):
        product_object = apps.get_model("main", "Product")
        product_wishlist_object = apps.get_model(
            "main", "ProductsAddedToWishlist")

        total_atwi = 0
        products = product_object.objects.filter(seller=self)

        for product in products:
            total_atwi += product_wishlist_object.objects.filter(
                product=product).count()

        product_wishlists = []
        for product in products:
            product_wishlists += product_wishlist_object.objects.filter(
                product=product)

        lastweeks_wishlists = []
        for product_wishlist in product_wishlists:
            delta = product_wishlist.time.astimezone(
                tz=None).day - timezone.now().astimezone(tz=None).day
            if delta >= -7:
                lastweeks_wishlists.append(product_wishlist)

        return total_atwi, lastweeks_wishlists
