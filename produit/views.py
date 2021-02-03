from django.shortcuts import render
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import allowed_users, admin_only

from produit.models import Produit

from django.http import HttpResponse
# Create your views here.
@login_required(login_url='acces')
#@allowed_users(allowed_roles=['admin','customer'])
#@admin_only
def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()

    client_total = clients.count()

    commande_total = commandes.count()

    commande_livre=commandes.filter(status='Livre').count()
    commande_en_cours=commandes.filter(status='En instance').count()

    context={'commandes':commandes,
             'clients':clients,
             'client_total':client_total,
             'commande_total':commande_total,
             'commande_livre':commande_livre,
             'commande_en_cours':commande_en_cours
            }
    return render(request,'produit/acceuil.html',context)
#    return render(request, 'dashboard.html', context)

@login_required(login_url='acces')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Produit.objects.all()

	return render(request, 'produit/produit.html', {'products':products})