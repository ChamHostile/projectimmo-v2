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
def annonceHome(request):
    query_ville = request.GET.get('query_ville')
    query_location = request.GET.get('query_location')
    query_locataires = request.GET.get('query_locataires')
    lastannonce = Annonce.objects.all().order_by('-id')[:6]
    image = ImageLogement.objects.all()
    context = {'annonce': lastannonce, 'image': image}
    return render(request, 'annonce/search/annonceHome.html', context)

def searchPage(request):
    myFilter = Annonce.objects.all()
    image = ImageLogement.objects.all()
    query_ville = request.GET.get('query_ville')
    query_location = request.GET.get('query_location')
    query_locataires = request.GET.get('query_locataires')

    if query_ville != '' and query_ville is not None:
        myFilter = myFilter.filter(address__ville__icontains=query_ville)

    if query_locataires != '' and query_locataires is not None:
        myFilter = myFilter.filter(nombre_personne=query_locataires)

    if query_location != '' and query_location is not None:
        myFilter = myFilter.filter(dureeLocationMaxi=query_location)

    if query_ville != '' and query_ville is not None and query_locataires != '' and query_locataires is not None:
        myFilter = myFilter.filter(address__ville__icontains=query_ville, nombre_personne=query_locataires)

    if query_ville != '' and query_ville is not None and query_locataires != '' and query_locataires is not None and \
            query_location != '' and query_location is not None:
        myFilter = myFilter.filter(address__ville__icontains=query_ville, nombre_personne=query_locataires,
                                   dureeLocationMaxi = query_location)

    context = {'annonces': myFilter, 'image':image}
    return render(request, 'annonce/search/search_page.html', context)

def detail_annonce(request, pk):
    myObject = Annonce.objects.get(id=pk)
    image = ImageLogement.objects.all()
    context = {'annonce': myObject, 'myImages': image}
    return render(request, 'annonce/search/annonce_result.html', context)