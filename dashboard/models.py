# Imports

from django.db.models.base import Model
from django.utils import timezone
from django.db import models

from authentication.models import CustomUser
from main.models import Product

# Models


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user}'s cart"

    def get_total_items(self):
        return self.products.all().count()

    def get_total_shipping(self):
        total = 0
        for product in self.products.all():
            total += product.shipping_price

        return total

    def get_total_price(self):
        total = 0
        for product in self.products.all():
            total += product.price

        return total

    def get_total_cost(self):
        total = 0
        for product in self.products.all():
            total += product.shipping_price
            total += product.price

        return total

    def create_order(self, request):
        sellers = []

        for product in self.products.all():
            if product.seller not in sellers:
                sellers.append(product.seller)

        for seller in sellers:
            order = Order.objects.create(user=self.user)

            for product in self.products.all():
                if product.seller == seller:
                    order.products.add(product)
                    self.products.remove(product)
                    product.sold += 1
                    product.revenue += product.price + product.shipping_price
                    product.save()

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
            self.save()


class Watchlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    last_updated = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s watchlist"

    def update(self):
        arr = []
        self.last_updated = timezone.now()
        self.save()
        for product in self.products.all():
            if product.last_updated is not None:
                date_time_delta = product.last_updated - self.last_updated
                if date_time_delta.days < -7:
                    if product in arr:
                        arr.remove(product)
                else:
                    if product not in arr:
                        arr.append(product)
            else:
                arr.append(product)

        return arr

    def updated_items_count(self):
        return len(self.update())


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.user}'s wishlist"


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    time_of_order = models.DateTimeField(default=timezone.now())
    status = models.CharField(max_length=255, choices=[
        ("Packaging", "Packaging"),
        ("Delivering", "Delivering"),
        ("Delivered", "Delivered")
    ], default="Packaging")

    name = models.CharField(default="",  max_length=255)
    email = models.EmailField(default="", max_length=254)
    contact = models.CharField(default="",  max_length=255)
    address = models.CharField(default="",  max_length=255)
    zip_code = models.CharField(default="",  max_length=32)
    country = models.CharField(default="",  max_length=32)
    state_province = models.CharField(default="",  max_length=32)
    city = models.CharField(default="",  max_length=32)

    payment_made = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}'s order no. {self.id}."

    def get_seller_revenue(self, user):
        seller = CustomUser.objects.get(user=user)

        total_product_price = 0
        total_shipping = 0
        total_revenue = 0

        for product in self.products.all():
            if product.seller == seller:
                total_product_price += product.price
                total_shipping += product.shipping_price

                total_revenue += product.shipping_price
                total_revenue += product.price

        return total_product_price, total_shipping, total_revenue
