from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        views.CustomLoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("logout/", views.LogoutView.as_view(next_page="main_page"), name="logout"),
    path("register/", views.SignUpView.as_view(), name="register"),
    path("edit/", views.UserProfileUpdateView.as_view(), name="edit"),
    path(
        "password_change/",
        views.CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
]
