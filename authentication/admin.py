from django.contrib import admin
from .models import VerifiedUser

# Register your models here.


class VerifiedUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(VerifiedUser, VerifiedUserAdmin)
