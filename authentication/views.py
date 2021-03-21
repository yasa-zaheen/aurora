# Imports

from django.shortcuts import render

# Views.


def sign_in(response):
    context = {}
    return render(response, "authentication/sign_in.html", context)


def sign_up(response):
    context = {}
    return render(response, "authentication/sign_up.html", context)


def forgot_password(response):
    context = {}
    return render(response, "authentication/forgot_password.html", context)


def update_password(response):
    context = {}
    return render(response, "authentication/update_password.html", context)
