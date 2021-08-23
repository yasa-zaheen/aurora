from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    huid = models.CharField(default="",  max_length=32)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
