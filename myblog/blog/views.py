from django.shortcuts import render
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
