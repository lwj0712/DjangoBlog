from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, UserUpdateForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import CustomUser



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('registration:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        # 추가적인 로직을 통해 다른 URL로 리디렉션할 수 있습니다.
        return reverse_lazy("accounts:login")


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("blog:post_list")


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = "registration/profile_edit.html"
    success_url = reverse_lazy('blog:post_list')

    def get_object(self, queryset=None):
        return self.request.user