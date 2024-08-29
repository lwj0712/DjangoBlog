from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('write/', views.PostCreateView.as_view(), name='post_create'),
    path('edit/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('search/<str:tag>/', views.PostSearchView.as_view(), name='post_search'),
    path('comment/<int:post_pk>/add/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:comment_pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:post_pk>/<int:comment_pk>/reply/', views.CommentReplyView.as_view(), name='comment_reply'),
]
