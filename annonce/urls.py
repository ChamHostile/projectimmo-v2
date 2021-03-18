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
    path('annonce/dashboard/loyer/<str:pk>/', views.loyer_view, name='dashboard-loyer'),
    path('annonce/dashboard/photos/<str:pk>/', views.image_view, name='dashboard-image'),
    path('annonce/dashboard/photos/delete/<str:pk>/', views.delete_image, name='delete-image'),
    path('annonce/dashboard/calendrier/<str:pk>/', views.calendrier, name='dashboard-calendrier'),
    path('annonce/dashboard/calendrier/create', views.create_calendrier, name='create-calendrier'),
    path('annonce/dashboard/calendrier/edit/<str:pk>/', views.edit_calendrier, name='calendrier-edit'),
    path('annonce/dashboard/conditions/<str:pk>/', views.condition_view, name='dashboard-condition'),
    path('annonce/dashboard/diagnostic/<str:pk>/', views.diagnsotic_view, name='dashboard-diagnostic'),
    path('annonce/dashboard/coordonnee_user/<str:pk>/', views.user_view_dashboard, name='dashboard-usercoord'),

]