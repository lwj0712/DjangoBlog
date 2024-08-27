from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DetailView,
    UpdateView, 
    DeleteView,
)


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')



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



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class PostCreateView(LoginRequiredMixin, CreateView):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'blog/post_form.html', {'form': form})
    

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'id': self.object.id})
    


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('post_list')


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(category__name__icontains=tag).order_by('-created_at')