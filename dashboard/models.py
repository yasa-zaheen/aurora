# Imports

from django.db import models

from authentication.models import CustomUser
from main.models import Product

# Models


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

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
