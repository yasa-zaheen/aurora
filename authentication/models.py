from django.contrib.auth.models import User
from django.db import models

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
