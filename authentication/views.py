# Imports

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator


from django.shortcuts import redirect, render, reverse
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.http.response import HttpResponsePermanentRedirect


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
        email = request.POST["username"]
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

    return render(request, "authentication/sign_up.html", status=status)


def sign_out(request):

    if request.user.is_anonymous:
        return HttpResponsePermanentRedirect(reverse("authentication:sign_in"))
    else:
        logout(request)


def password_reset(request):

    if request.method == "POST":
        email = request.POST["email"]
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
    return render(request, "authentication/password_reset.html", context)


def password_change(request, uidb64, token):

    user = User.objects.get(id=int.from_bytes(
        urlsafe_base64_decode(uidb64), "big"))

    if PasswordResetTokenGenerator().check_token(user, token) == True:
        if request.method == "POST":
            if request.POST["password"] != request.POST["confirm_password"]:
                messages.add_message(
                    request, messages.ERROR, 'Passwords do not match')
            else:
                user.set_password(request.POST["password"])
                user.save()
                messages.add_message(
                    request, messages.SUCCESS, 'Passwords reset successfully!')
                return redirect(reverse("authentication:sign_in"))
    else:
        return redirect(reverse("main:index"))

    context = {}
    return render(request, "authentication/password_change.html", context)


def verify_user(request):
    context = {}
    return
