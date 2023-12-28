# blog/urls.py
from django.urls import path
from .views import fetch_all_users

urlpatterns = [
    path('', fetch_all_users, name='fetch_all_users'),
]