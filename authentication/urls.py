# Imports

from django.urls import path
from . import views

# URL Configurations

app_name = "authentication"
urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("update_password/", views.update_password, name="update_password")
]
