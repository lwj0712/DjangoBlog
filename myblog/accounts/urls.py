from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, UserProfileUpdateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='main_page'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('edit/', UserProfileUpdateView.as_view(), name='edit'),
]
