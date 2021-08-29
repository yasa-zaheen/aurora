# Imports

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
    price = models.FloatField()
    seller = models.ForeignKey(
        CustomUser, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        SubCategory, null=True, on_delete=models.SET_NULL)

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
    payments = models.CharField(max_length=255)

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

    def ratings(self):
        import math

        total = 0
        for i in Review.objects.filter(product=self):
            total += i.ratings

        try:
            return math.ceil(total / Review.objects.filter(product=self).count())
        except ZeroDivisionError:
            return 0

    # product_type = models.ForeignKey(
    #     ProductType, null=True, on_delete=models.SET_NULL)
    # filters = models.ManyToManyField(
    #     Filter)
    # sub_category = models.ForeignKey(
    #     SubCategory, null=True, on_delete=models.SET_NULL)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.product}"
