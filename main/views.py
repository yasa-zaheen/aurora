# Imports

from django.shortcuts import render
from main.models import *

from main.webscraper import permission
from main.product_types import *
from main.filters import *

# Views


def index(response):
    all_categories = Category.objects.order_by('name')

    context = {
        'all_categories': all_categories
    }

    return render(response, "main/index.html", context)


def products(response):

    all_categories = Category.objects.order_by('name')

    context = {
        'all_categories': all_categories
    }

    return render(response, "main/products.html", context)


def product(response):

    all_categories = Category.objects.order_by('name')

    context = {
        'all_categories': all_categories

    }

    return render(response, "main/product.html", context)


def category(response, id):

    category = Category.objects.get(id=id)
    sub_categories = SubCategory.objects.filter(
        category=category).order_by('name')

    all_categories = Category.objects.order_by('name')

    context = {
        "category": category,
        "sub_categories": sub_categories,
        'all_categories': all_categories

    }

    return render(response, "main/category.html", context)


def brand(response):

    context = {}
    return render(response, "main/brand.html", context)


def sub_category(response, id):

    all_categories = Category.objects.order_by('name')

    sub_category = SubCategory.objects.get(id=id)
    product_types = ProductType.objects.filter(
        sub_category=sub_category, parent_product_type="").order_by('name')

    context = {
        "sub_category": sub_category,
        "product_types": product_types,
        'all_categories': all_categories

    }
    return render(response, "main/sub_category.html", context)


def product_type(response, id):

    all_categories = Category.objects.order_by('name')

    filter_categories = []
    filter_categorys_num = 0

    product_type = ProductType.objects.get(id=id)
    children_product_types = ProductType.objects.filter(
        parent_product_type=product_type.name, sub_category=product_type.sub_category)
    filters = Filter.objects.filter(
        product_type=product_type).order_by('filter_category', 'name')

    if len(children_product_types) != 0:
        children_product_types_exists = True
    else:
        children_product_types_exists = False

    for filter in filters:

        if filter.filter_category in filter_categories:
            pass
        else:
            filter_categories.append(filter.filter_category)
            filter_categorys_num += 1

    context = {
        "product_type": product_type,
        "children_product_types": children_product_types,
        "filters": filters,
        "filter_categories": filter_categories,
        "children_product_types_exists": children_product_types_exists,
        'all_categories': all_categories

    }
    return render(response, "main/product_type.html", context)


def seller(response):
    context = {}
    return render(response, "main/product_seller.html", context)


def cart(response):
    context = {}
    return render(response, "main/cart.html", context)


def dashboard(response):
    context = {}
    return render(response, "main/dashboard.html", context)


# permission()

# add_product_types()

# filters_for_product_type()
