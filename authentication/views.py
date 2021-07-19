# Imports

from django.shortcuts import redirect, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Views

def sign_in(request):

    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
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

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if username == "" or email == "" or password == "" or confirm_password == "":
            messages.add_message(
                request, messages.ERROR, 'Fields cannot be empty.')
        else:
            try:
                User.objects.get(username=username)

                messages.add_message(
                    request, messages.ERROR, 'Username taken.')

            except:

                if password != confirm_password:
                    messages.add_message(
                        request, messages.ERROR, 'Passwords do not match')
                else:
                    user = User.objects.create(
                        username=username, email=email, password=password)
                    user.save()

                    redirect(reverse("dashboard:home"))

    context = {}
    return render(request, "authentication/sign_up.html", context)


def sign_out(response):
    logout(response)
    return redirect(reverse("main:index"))


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
