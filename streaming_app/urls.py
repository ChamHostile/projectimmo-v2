from django.urls import path

from . import views

urlpatterns = [
    path('streaming_page', views.streaming_page, name='streaming_page'),
    path('streaming_index/<int:pk>', views.streaming_index, name='streaming_index'),
]