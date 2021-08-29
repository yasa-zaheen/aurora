# Imports

from django.contrib import admin
from main.models import *

# Admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_photographer')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_photographer', "category")
    list_filter = ['category']


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',
                    "sub_category", "get_category")
    list_filter = ['sub_category', ]


class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', "filter_category", 'product_type')
    list_filter = ["product_type", ]


class ProductAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


# Registration
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Filter, FilterAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
