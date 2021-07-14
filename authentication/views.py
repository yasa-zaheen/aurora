# Imports

from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib import messages

import time


# Views

def sign_in(request):

    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                time.sleep(5)
                login(request, user)
                return redirect("/dashboard/home")
            else:
                try:
                    user = User.objects.get(username=username)
                    if user is not None:
                        messages.add_message(
                            request, messages.WARNING, 'Password is incorrect.')

                except:
                    if user is None:
                        messages.add_message(
                            request, messages.ERROR, 'There is no account under this username.')

        context = {}
        return render(request, "authentication/sign_in.html", context)
    else:
        return redirect("/dashboard/home")


def sign_up(request):
    context = {}
    return render(request, "authentication/sign_up.html", context)


def forgot_password(request):
    context = {}
    return render(request, "authentication/forgot_password.html", context)


def update_password(request):
    context = {}
    return render(request, "authentication/update_password.html", context)
