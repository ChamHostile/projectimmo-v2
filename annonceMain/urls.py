from django.urls import path
from . import views


urlpatterns = [
    path('annonce/searchPage/', views.searchPage, name='search_annonce'),
    path('annonce/detail_annonce/<str:pk>', views.detail_annonce, name='detail_annonce'),
]