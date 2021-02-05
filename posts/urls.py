from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('create_post/', views.create_post_view, name='create_post'),
]