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
    query = request.GET.get('q')
    annonce_address = AddressAnnonce.objects.filter(ville=query)
    annonces = annonce_address.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=annonces)
    annonces = myFilter.qs

    context={'annonces': annonces, 'myFilter': myFilter}
    return render(request,'annonce/search/search_page.html',context)

