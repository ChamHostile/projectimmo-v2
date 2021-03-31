from django.urls import path
from . import views


urlpatterns = [
    path('annonce/searchPage/', views.searchPage, name='search_annonce'),
]