from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('creer-annonce', views.create_annonce, name='creer-annonce'),

]