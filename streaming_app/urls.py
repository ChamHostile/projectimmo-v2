from django.urls import path

from . import views

urlpatterns = [
    path('streaming_index', views.streaming_index, name='streaming_index'),
]