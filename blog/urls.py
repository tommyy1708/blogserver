# blog/urls.py
from django.urls import path
from .views import PostList, PostDetail
from .views import fetch_username

urlpatterns = [
    path('console/', fetch_username, name='fetch_username'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]