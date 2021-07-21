from django.contrib.auth.models import User
from django.db import models
import hashlib

# Create your models here.


class VerifiedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    huid = models.CharField(max_length=32, default="")
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
