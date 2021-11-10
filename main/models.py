# Imports

from django.db.models import base
from django.db.models.fields import FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone, tree
from django.db import models
from django.db.models.deletion import SET_NULL

from authentication.models import CustomUser


# Models


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True,
                              upload_to="categories")
    image_photographer = models.CharField(max_length=255)
    image_photographer_url = models.URLField(max_length=200)
    show_brand_in_sub_category = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]


class SubCategory(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(blank=True, null=True,
                              upload_to="sub-categories")
    image_photographer = models.CharField(
        max_length=255, blank=True, null=True,)
    image_photographer_url = models.URLField(
        max_length=200, blank=True, null=True,)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    sub_category_title = models.CharField(
        max_length=30, default="Product Types")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"
        ordering = ["name"]


class ProductType(models.Model):
    name = models.CharField(max_length=30)
    image = models.URLField(blank=True, null=True)
    image_photographer = models.CharField(
        max_length=255, null=True, blank=True)
    image_photographer_url = models.URLField(max_length=200, blank=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=SET_NULL, null=True)
    parent_product_type = models.CharField(
        blank=True, max_length=30, default="")

    def __str__(self):
        return self.name

    def get_category(self):
        return self.sub_category.category

    class Meta:
        verbose_name_plural = "Product Types"
        ordering = ["name"]


class Filter(models.Model):
    name = models.CharField(max_length=30)
    filter_category = models.CharField(max_length=30, null=True, blank=True)
    product_type = models.ForeignKey(
        ProductType, on_delete=SET_NULL, null=True)
    background_color = models.CharField(max_length=9, default="#fafafa")
    foreground_color = models.CharField(max_length=9, default="#2f2f2f")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["product_type", "filter_category", "name"]


class Product(models.Model):
    name = models.CharField(max_length=255)
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(
        auto_now=True)
    sold = models.IntegerField(default=0)
    revenue = models.FloatField(default=0)

    price = models.FloatField()
    old_price = models.FloatField(blank=True, null=True)
    price_last_updated = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    stock = models.IntegerField()
    old_stock = models.IntegerField(blank=True, null=True)
    stock_last_updated = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)

    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        SubCategory, null=True, on_delete=models.SET_NULL)
    product_type = models.ForeignKey(
        ProductType, null=True, on_delete=models.SET_NULL)
    filters = models.ManyToManyField(
        Filter, null=True, editable=False)

    image_1 = models.ImageField(blank=True, null=True,
                                upload_to="products")
    image_2 = models.ImageField(blank=True, null=True,
                                upload_to="products")
    image_3 = models.ImageField(blank=True, null=True,
                                upload_to="products")
    image_4 = models.ImageField(blank=True, null=True,
                                upload_to="products")

    condition = models.CharField(max_length=255)
    shipping = models.CharField(max_length=255)
    returns = models.CharField(max_length=255)

    product_does_not_ship_to = models.TextField()
    shipping_price = models.FloatField()
    product_location = models.TextField()

    payments_paypal = models.BooleanField(default=False)
    payments_master_card = models.BooleanField(default=False)
    payments_visa = models.BooleanField(default=False)
    payments_cod = models.BooleanField(default=False)
    features = models.TextField()

    def __str__(self):
        return self.name

    def payments(self):

        paypal = f"{'Paypal' if self.payments_paypal else ''}"
        visa = f"{'Visa' if self.payments_visa else ''}"
        mastercard = f"{'Mastercard' if self.payments_master_card else ''}"

        sys = [paypal, visa, mastercard]
        msg = ""

        for i in sys:
            if i != "":
                msg += f"{i}, "

        return f"{msg[:-2]}."

    def ratings(self):
        import math

        total = 0
        for i in Review.objects.filter(product=self):
            total += i.ratings

        try:
            return math.ceil(total / Review.objects.filter(product=self).count())
        except ZeroDivisionError:
            return 0

    def change_price(self, price):
        self.old_price = self.price
        self.price = price
        self.last_updated = timezone.now()
        self.price_last_updated = timezone.now()

        self.save()

    def change_stock(self, stock):
        self.old_stock = self.stock
        self.stock = stock
        self.last_updated = timezone.now()
        self.price_last_updated = timezone.now()

        self.save()

    def change_in_price(self):
        return self.price - self.old_price

    def change_in_stock(self):
        return self.stock - self.old_stock

    def price_recently_updated(self):

        if self.price_last_updated is not None:
            current_time = timezone.now()
            date_time_delta = self.price_last_updated - current_time
            if date_time_delta.days < -7:
                return False
            else:
                return True
        else:
            return False

    def stock_recently_updated(self):

        if self.stock_last_updated is not None:
            current_time = timezone.now()
            date_time_delta = self.stock_last_updated - current_time
            if date_time_delta.days < -7:
                return False
            else:
                return True
        else:
            return False

    def edit_product(self, request):

        # General Information

        self.name = request.POST["name"]
        self.condition = request.POST["condition"]
        self.returns = request.POST["returns"]
        self.payments = request.POST["payments"]
        self.product_location = request.POST["product-location"]
        self.features = request.POST["features"]

        # Shipping Information

        self.shipping = request.POST["shipping"]
        self.shipping_price = request.POST["shipping-price"]
        self.product_does_not_ship_to = request.POST["product-does-not-ship-to"]

        # Images

        if "image-1" in request.FILES:
            self.image_1 = request.FILES["image-1"]

        if "image-2" in request.FILES:
            self.image_2 = request.FILES["image-2"]

        if "image-3" in request.FILES:
            self.image_3 = request.FILES["image-3"]

        if "image-4" in request.FILES:
            self.image_4 = request.FILES["image-4"]

        # Price

        if self.price != request.POST["price"]:
            self.change_price(request.POST["price"])

        # Stock

        if self.stock != request.POST["stock"]:
            self.change_stock(request.POST["stock"])

        self.save()


class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.product}"
