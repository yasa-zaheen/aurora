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
        return self.products.count()

    def get_total_shipping(self):
        total = 0
        for product in self.products:
            total += product.shipping_price

        return total

    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price

        return total

    def get_total_cost(self):
        return self.get_total_shipping + self.get_total_price
