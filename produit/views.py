from django.shortcuts import render, redirect
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import allowed_users, admin_only

from produit.models import Produit
from .forms import ProductForm

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

def products_create(request):
    form = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    context = {'form': form}

    return render(request,'produit/creer_produit.html',context)

def products_update(request, pk):
    product = Produit.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/produits')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request,'produit/creer_produit.html',context)

def products_delete(request, pk):
    product = Produit.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/produits')
    context = {'product': product}
    return render(request, 'produit/delete_produit.html', context)