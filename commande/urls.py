"""Projet_locationimmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.liste_commandes),
    path('ajout_commande/',views.ajouter_commande, name='ajout_commande'),
    path('modifie_commande/<str:pk>', views.modifier_commande, name='modifie_commande'),
    path('supprime_commande/<str:pk>', views.supprimer_commande, name='supprime_commande'),
]