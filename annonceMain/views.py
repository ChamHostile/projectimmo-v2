from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import *
from annonce.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from annonce.models import *
from annonce.filters import OrderFilter
from django.contrib.auth.decorators import login_required
from itertools import chain


# Create your views here.
def searchPage(request):
    query_ville = request.GET.get('ville')
    query_location = request.GET.get('location')
    query_locataires = request.GET.get('locataires')
    ville_annonce = []
    myFilter = []
    list_annonce = []
    if query_ville == "":
        ville_annonce = AddressAnnonce.objects.all()
        for obj in ville_annonce:
            list_annonce.append(obj.annonce)
            print(list_annonce)
    else:
        ville_annonce = AddressAnnonce.objects.filter(ville=query_ville)
        for obj in ville_annonce:
            list_annonce.append(obj.annonce)
            print(list_annonce)

    if query_locataires == '' :
        myFilter = list_annonce.filter(dureeLocationMini=query_location)
    elif query_location == '':
        myFilter = list_annonce.filter(dureeLocationMini=query_locataires)
    elif query_location == '' and query_locataires == '':
        myFilter = list_annonce.objects.all()
    else:
        myFilter = list_annonce.filter(dureeLocationMini=query_location, nombre_personne=query_locataires)

    context = {'annonces': list_annonce}
    return render(request, 'annonce/search/search_page.html', context)





