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
        userForm = CreateUserForm(request.POST)
        annonceForm = AnnonceForm(request.POST)

        if userForm.is_valid() or annonceForm.is_valid():

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