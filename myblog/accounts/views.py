from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView



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