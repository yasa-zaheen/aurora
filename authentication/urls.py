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

    path("password_reset/", views.password_reset, name="password_reset")
]
