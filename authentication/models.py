from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="profile_images", default="profile_images/user.png")
    huid = models.CharField(default="",  max_length=32)
    is_verified = models.BooleanField(default=False)

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
