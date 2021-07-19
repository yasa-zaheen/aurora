# Imports

from django.contrib import auth
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# URL Configurations

app_name = "authentication"
urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_out/", views.sign_out, name="sign_out"),

    path("password_reset/", views.password_reset, name="password_reset"),
    path("password_change/<uidb64>/<token>/",
         views.password_change, name="password_change")
]
