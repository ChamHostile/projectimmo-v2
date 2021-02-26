from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('creer-annonce', views.create_annonce, name='creer-annonce'),
    path('login-annonce', views.login_user, name='login-annonce'),
    path('logout-annonce', views.logout_annonce, name='logout-annonce'),
    path('logged-annonce', views.logged_annonce, name='logged-annonce'),
    path('annonce/dashboard', views.dashboard_view, name='dashboard-annonce'),
    path('annonce/dashboard/description', views.description_view, name='dashboard-description'),

]