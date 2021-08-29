# Imports


from authentication.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http.response import HttpResponsePermanentRedirect
from django.conf import settings

import hashlib
import os


# Views
def sign_in(request):

    status = 200
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("dashboard:home"))
            else:
                if User.objects.filter(username=username).count() == 0:
                    messages.add_message(
                        request, messages.ERROR, "Username does not belong to any account.")
                    status = 401
                else:
                    messages.add_message(
                        request, messages.ERROR, "Password is incorrect.")
                    status = 401

        context = {}
        return render(request, "authentication/sign_in.html", context, status=status)

    else:
        return HttpResponsePermanentRedirect(reverse("dashboard:home"))


def sign_up(request):

    status = 200

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).count() != 0:
            messages.add_message(
                request, messages.ERROR, "This username has been taken by another account.")
            status = 409
        elif User.objects.filter(email=email).count() != 0:
            messages.add_message(
                request, messages.ERROR, "An account has already been opened using this email.")
            status = 409
        elif len(password) < 8:
            messages.add_message(
                request, messages.ERROR, "Password must be atleast 8 characters in length.")
            status = 406
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()

            custom_user = CustomUser.objects.create(
                user=user, huid=hashlib.md5(str(user.id).encode()).hexdigest(), is_verified=False)
            custom_user.save()

            send_mail(
                subject="Verify Account",
                message=f"{custom_user.huid}",
                from_email="yasazaheen728@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,
                html_message=f"<a href='http://127.0.0.1:8000/auth/verify_user/{custom_user.huid}/' >Click here</a>"
            )

            login(request, user)
            return redirect(reverse("dashboard:home"))

    return render(request, "authentication/sign_up.html", status=status)


def sign_out(request):

    if request.user.is_anonymous:
        return HttpResponsePermanentRedirect(reverse("authentication:sign_in"))
    else:
        logout(request)
        return HttpResponsePermanentRedirect(reverse("authentication:sign_in"))


def password_reset(request):

    status = 200

    if request.method == "POST":
        email = request.POST["email"]

        if User.objects.filter(email=email).count() == 0:
            messages.add_message(
                request, messages.ERROR, "Email does not belong to any account.")
            status = 404
        else:
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode((user.id).to_bytes(2, "big"))
            token = PasswordResetTokenGenerator().make_token(user)

            send_mail(
                subject="Password Reset Confirmation",
                message=f"{uidb64}/{token}",
                from_email="yasazaheen728@gmail.com",
                recipient_list=[email],
                fail_silently=False,
                html_message=f"<a href='http://127.0.0.1:8000/auth/password_change/{uidb64}/{token}/' >Click here</a>"
            )

            messages.add_message(
                request, messages.SUCCESS, 'Email has been sent. Please check your inbox.')

    context = {}
    return render(request, "authentication/password_reset.html", context, status=status)


def password_change(request, uidb64, token):

    status = 200

    user = User.objects.get(id=int.from_bytes(
        urlsafe_base64_decode(uidb64), "big"))

    if PasswordResetTokenGenerator().check_token(user, token) == True:
        if request.method == "POST":
            password = request.POST["password"]

            if len(password) < 8:
                messages.add_message(
                    request, messages.ERROR, "Password must be atleast 8 characters in length.")
                status = 406
            else:
                user.set_password(password)
                user.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Passwords reset successfully!')
                return redirect(reverse("authentication:sign_in"))
    else:
        return redirect(reverse("main:index"))

    context = {}
    return render(request, "authentication/password_change.html", context, status=status)


def verify_user(request, huid):

    custom_user = CustomUser.objects.get(huid=huid)

    if custom_user.is_verified:
        context = {
            "message": "Your account has already been verified!"
        }
        return render(request, "authentication/verify_user.html", context, status=200)
    else:
        custom_user.is_verified = True
        custom_user.save()
        context = {
            "message": "Your account has been verified!"
        }
        return render(request, "authentication/verify_user.html", context, status=400)
