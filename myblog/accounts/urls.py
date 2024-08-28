from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import SignUpView, UserProfileUpdateView, CustomLoginView, CustomPasswordChangeView


app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='main_page'), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    path('edit/', UserProfileUpdateView.as_view(), name='edit'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
