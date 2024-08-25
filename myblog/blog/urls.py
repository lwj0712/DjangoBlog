from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    PostSearchView
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('write/', PostCreateView.as_view(), name='post_create'),
    path('edit/<int:id>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:id>/', PostDeleteView.as_view(), name='post_delete'),
    path('search/<str:tag>/', PostSearchView.as_view(), name='post_search'),
]
