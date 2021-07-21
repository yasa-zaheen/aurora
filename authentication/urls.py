# Imports

from django.urls import path
from . import views

# URL Configurations

app_name = "authentication"
urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_out/", views.sign_out, name="sign_out"),

    path("password_reset/", views.password_reset, name="password_reset"),
    path("password_change/<uidb64>/<token>/",
         views.password_change, name="password_change"),

    path("verify_user/<uidb64>", views.verify_user, name="verify_user")
]
