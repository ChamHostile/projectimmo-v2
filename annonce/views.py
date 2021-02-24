from django.shortcuts import render, redirect
from .models import Annonce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import AnnonceForm, CreateUserForm
from account.models import Account
from .models import Annonce
# Create your views here.
def create_annonce(request):

    form = AnnonceForm()
    userForm = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            cleanedEmail = form.cleaned_data['email']
            emailUser = Account.objects.include(email=cleanedEmail)
            if emailUser:


            form.save()
            return redirect('/')
    else:
        form = CreateUserForm()

    if request.method == 'POST':
        form = AnnonceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AnnonceForm()

    context = {'form': form, 'userForm': userForm}

    return render(request,'annonce/creer-annonce.html',context)