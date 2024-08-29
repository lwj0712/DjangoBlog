from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, UserUpdateForm, CustomPasswordChangeForm



class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("blog:post_list")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:login")


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy('blog:post_list')

    def get_object(self, queryset=None):
        return self.request.user
    

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'accounts/password_change_form.html'