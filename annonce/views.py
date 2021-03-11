from pyexpat.errors import messages

from django.shortcuts import render, redirect
from .models import Annonce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .decorators import unauthenticated_user
from .forms import *
from account.models import Account
from .models import *
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

@unauthenticated_user
def inscriptionPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
                user=form.save()
                return redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

@unauthenticated_user
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
            annonceForm.save()
            newAnnonce = annonceForm.save()
            user_created(Annonce, request)
            return redirect(reverse('dashboard-annonce', kwargs={'pk':newAnnonce.id}))

    else:
        annonceForm = AnnonceForm()


    context = {'annonceForm': annonceForm}

    return render(request, 'annonce/logged-annonce.html', context)

@login_required
def dashboard_view(request, pk):
    myObject = Annonce.objects.get(id=pk)
    context = {'obj': myObject}
    return render(request, 'annonce/dashboard/dashboard.html', context)

@login_required
def gerer_annonce(request):
    requete = request.user
    myObject = Annonce.objects.filter(user=request.user)
    context = {'obj': myObject}
    return render(request, 'annonce/dashboard/gerer-annonce.html', context)

@login_required
def description_view(request, pk):
    form = DescriptionForm()
    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    if request.method =='POST':
        form = DescriptionForm(request.POST, instance=myObject)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = DescriptionForm(instance=myObject)
    context = {'form': form, 'obj': myObject, 'requete': requete}
    return render(request,'annonce/dashboard/description.html',context)

    context = {'descriptionForm': DescriptionForm}

@login_required
def equipment_view(request, pk):
    form = EquipmentForm()
    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    if request.method =='POST':
        form = EquipmentForm(request.POST, instance=myObject)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = EquipmentForm(instance=myObject)
    context = {'form': form, 'requete': requete, 'obj': myObject}
    return render(request,'annonce/dashboard/equipements.html',context)

    context = {'descriptionForm': DescriptionForm}

@login_required
def dureeLocation_view(request, pk):
    dureeMaxi = request.POST.get('selectMax')
    dureeMini = request.POST.get('minSelect')
    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    if request.method =='POST':
        myObject.dureeLocationMini = dureeMini
        myObject.save()
        myObject.dureeLocationMaxi = dureeMaxi
        myObject.save()

    context = {'requete': requete, 'obj': myObject}
    return render(request,'annonce/dashboard/dureeLocation.html',context)

    context = {'descriptionForm': DescriptionForm}

@login_required
def loyer_view(request, pk):
    allCharges = Charges.objects.all()
    form = FormFeature()
    valueCharges = request.POST.getlist('myRadio')

    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    if request.method =='POST':
        form = FormFeature(request.POST, instance=myObject)
        for thisCharge in allCharges:
            for value in valueCharges:
                if thisCharge.nom == value:
                    myObject.charges.add(thisCharge)
        if form.is_valid():
            form.save()
        else:
            form = FormFeature(instance=myObject)
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

    context = {'requete': requete, 'obj': myObject, 'charges': allCharges, 'form': form}
    return render(request,'annonce/dashboard/loyer.html',context)

    context = {'descriptionForm': DescriptionForm}