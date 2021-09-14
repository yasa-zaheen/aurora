# Imports

from django.contrib import admin
from dashboard.models import *

# Admin


class CartAdmin(admin.ModelAdmin):
    pass


class WatchlistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
