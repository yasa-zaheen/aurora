# Imports

from django.shortcuts import render

# Views


def home(response):
    context = {}
    return render(response, 'dashboard/home.html', context)
