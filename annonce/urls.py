from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('creer-annonce', views.create_annonce, name='creer-annonce'),
    path('register', views.inscriptionPage, name='register'),
    path('login-annonce', views.login_user, name='login-annonce'),
    path('logout-annonce', views.logout_annonce, name='logout-annonce'),
    path('logged-annonce', views.logged_annonce, name='logged-annonce'),
    path('annonce/gerer-annonce', views.gerer_annonce, name='gerer-annonce'),
    path('annonce/dashboard/<str:pk>', views.dashboard_view, name='dashboard-annonce'),
    path('annonce/dashboard/description/<str:pk>/', views.description_view, name='dashboard-description'),
    path('annonce/dashboard/dureeLocation/<str:pk>/', views.dureeLocation_view, name='dashboard-dureelocation'),
    path('annonce/dashboard/equipment/<str:pk>/', views.equipment_view, name='dashboard-equipment'),

]