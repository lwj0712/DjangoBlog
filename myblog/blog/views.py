from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView, 
    DeleteView,
)


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']  # 최신 순으로 정렬
    paginate_by = 5 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        search_type = self.request.GET.get('search_type')

        if query:
            if search_type == 'title':
                queryset = queryset.filter(title__icontains=query)
            elif search_type == 'content':
                queryset = queryset.filter(content__icontains=query)
            elif search_type == 'author':
                queryset = queryset.filter(author__username__icontains=query)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.request.user.is_authenticated  # 로그인 여부 전달
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')  # 게시글 생성 후 리다이렉트할 URL

    def form_valid(self, form):
        # 폼이 유효할 때 현재 로그인한 사용자를 작성자로 설정
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# 게시글 수정 뷰
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:post_list')  # 삭제 후 리다이렉트할 URL
    template_name = 'blog/post_form.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, id=self.kwargs['id'])

    # 사용자가 해당 게시글의 작성자인지 확인하는 메서드
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # test_func이 False를 반환할 때 호출
    def handle_no_permission(self):
        return HttpResponseForbidden("권한이 없습니다.")


# 게시글 삭제 뷰
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')  # 삭제 후 리다이렉트할 URL
    template_name = 'blog/post_confirm_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Post, id=self.kwargs['id'])

    # 사용자가 해당 게시글의 작성자인지 확인하는 메서드
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # test_func이 False를 반환할 때 호출
    def handle_no_permission(self):
        return HttpResponseForbidden("권한이 없습니다.")


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(category__name__icontains=tag).order_by('-created_at')