from django.shortcuts import render, redirect
from .models import Annonce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .decorators import unauthenticated_user
from .forms import *
from account.models import Account
from .models import Annonce
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_created(model, request):
    obj = model.objects.latest('id')
    if obj.user is None:
        obj.user = request.user
    obj.save()

@unauthenticated_user
def create_annonce(request):

    form = AnnonceForm()
    userForm = CreateUserForm()


    if request.method == 'POST':
        userForm = CreateUserForm(request.POST)
        annonceForm = AnnonceForm(request.POST)

        if userForm.is_valid() and annonceForm.is_valid():
            user = userForm.save()
            annonceForm.save()
            Annonce.objects.create(
                user=user,
            )
            userForm.save()
            return redirect('/')
    else:
        userForm = CreateUserForm()
        annonceForm = AnnonceForm()

    context = {'annonceForm': annonceForm, 'userForm': userForm}

    return render(request,'annonce/creer-annonce.html',context)

def login_user(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('logged-annonce')

    context = {}
    return render(request, 'compte/login-annonce.html')

def logout_annonce(request):
    logout(request)
    return redirect('creer-annonce')

@login_required(login_url='login-annonce')
def logged_annonce(request):
    annonceForm = LoggedForm()


    if request.method == 'POST':
        annonceForm = AnnonceForm(request.POST)

        if annonceForm.is_valid():
            annonceForm.save()
            user_created(Annonce, request)
            return redirect('dashboard-annonce')

    else:
        annonceForm = AnnonceForm()


    context = {'annonceForm': annonceForm}

    return render(request, 'annonce/logged-annonce.html', context)

def dashboard_view(request):
    context = {}
    return render(request, 'annonce/dashboard/dashboard.html', context)

def description_view(request):
    form = DescriptionForm()
    requete = request.user
    myObject = Annonce.objects.filter(user=request.user).latest('id')
    if request.method =='POST':
        form = DescriptionForm(request.POST, instance=myObject)
        if form.is_valid():
            form.save()
            return redirect('dashboard-annonce')
    else:
        form = DescriptionForm(instance=myObject)
    context = {'form': form, 'obj': myObject, 'requete': requete}
    return render(request,'annonce/dashboard/description.html',context)

    context = {'descriptionForm': DescriptionForm}

def equipment_view(request):
    form = EquipmentForm()
    requete = request.user
    myObject = Annonce.objects.filter(user=request.user).latest('id')
    if request.method =='POST':
        form = EquipmentForm(request.POST, instance=myObject)
        if form.is_valid():
            form.save()
            return redirect('dashboard-annonce')
    else:
        form = EquipmentForm(instance=myObject)
    context = {'form': form, 'requete': requete, 'obj': myObject}
    return render(request,'annonce/dashboard/equipements.html',context)

    context = {'descriptionForm': DescriptionForm}

def dureeLocation_view(request):
    dureeMaxi = request.POST.get('selectMax')
    dureeMini = request.POST.get('minSelect')
    requete = request.user
    myObject = Annonce.objects.filter(user=requete).latest('id')
    if request.method =='POST':
        myObject.dureeLocationMini = dureeMini
        myObject.save()
        myObject.dureeLocationMaxi = dureeMaxi
        myObject.save()
        return redirect('dashboard-annonce')

    context = {'requete': requete}
    return render(request,'annonce/dashboard/dureeLocation.html',context)

    context = {'descriptionForm': DescriptionForm}