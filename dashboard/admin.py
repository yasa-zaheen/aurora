# Imports

from django.contrib import admin
from dashboard.models import *

# Admin


class CartAdmin(admin.ModelAdmin):
    pass


class WatchlistAdmin(admin.ModelAdmin):
    pass


class WishlistAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Order, OrderAdmin)
