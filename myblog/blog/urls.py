from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('write/', views.PostCreateView.as_view(), name='post_create'),
    path('edit/<int:id>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:id>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('search/<str:tag>/', views.PostSearchView.as_view(), name='post_search'),
    
]
