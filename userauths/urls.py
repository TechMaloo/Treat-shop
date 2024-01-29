from django.contrib import admin
from django.urls import path

from . import views

app_name = "userauths"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
]
