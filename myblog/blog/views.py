from django.shortcuts import render
from .models import Post
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
class MainPageView(TemplateView):
    template_name = 'main_page.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'