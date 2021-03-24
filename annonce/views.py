from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.views import View

from .models import Annonce
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

from .decorators import unauthenticated_user
from .forms import *
from account.models import Address
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

        # - validate both forms
        if userForm.is_valid() and annonceForm.is_valid():
            user = userForm.save()
            email = userForm.cleaned_data['email']
            annonce = annonceForm.save()

            # - associate new objects with newly created user to use in dashboard
            Annonce.objects.create(
                user=user,
            )
            Condition.objects.create(
                annonce=annonce,
            )
            Address.objects.create(
                account=user,
            )
            annonceForm.save()
            userForm.save()
            # path to view
                # - getting domain
                # - relative url to verif
                # - encode uid for security
                # - token
            uidb64=urlsafe_base64_encode(force_bytes(user.id))

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                            'uidb64':uidb64, 'token':token_generator.make_token(user)})

            activate_url = 'http://'+domain+link
            email_subject = 'Activez votre compte'
            email_body = 'Hi '+user.first_name + ' Cliquez sur ce lien pour vérifier votre compte\n' \
                         + activate_url

            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@lhoman.com',
                [email],
            )
            email.send(fail_silently=False)
            return redirect('/')
    else:
        userForm = CreateUserForm()
        annonceForm = AnnonceForm()

    context = {'annonceForm': annonceForm, 'userForm': userForm}

    return render(request,'annonce/creer-annonce.html',context)

class VerificationView(View):
    def get(self, request, uidb64, token):
        userId = urlsafe_base64_decode(uidb64)
        user = Account.objects.get(id=userId)
        user.is_active = True
        user.save()
        context = {'user': user}
        return redirect('creer-annonce')

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

@login_required
def dureeLocation_view(request, pk):
    # - getting value from the displayed select in template to update object
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

@login_required
def loyer_view(request, pk):
    allCharges = Charges.objects.all()
    form = FormLoyer()

    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    if request.method =='POST':
        form = FormLoyer(request.POST, instance=myObject)
        if form.is_valid():
            # veryfing if selected charges are in created charges objects, if so adding these charges
            # to the annonce
            for thisCharge in allCharges:
                valueCharges = request.POST.get('' + thisCharge.nom)
                if thisCharge.nom == valueCharges:
                    myObject.charges.add(thisCharge)
                else:
                    myObject.charges.remove(thisCharge)
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            form = FormLoyer(instance=myObject)


    context = {'requete': requete, 'obj': myObject, 'charges': allCharges, 'form': form}
    return render(request,'annonce/dashboard/loyer.html',context)

@login_required
def image_view(request, pk):
    myObject = Annonce.objects.get(id=pk)
    myImages = ImageLogement.objects.filter(annonce=myObject)
    if request.method == 'POST':
        length = request.POST.get('length')
        # managing multi image selection with filepond
        for file_num in range(0, int(length)):
            ImageLogement.objects.create(
                annonce=myObject,
                images=request.FILES.get(f'images{file_num}')
             )

    context = {'obj': myObject, 'images': myImages}
    return render(request,'annonce/dashboard/photos.html',context)


def delete_image(request, pk):
    deletedImage = ImageLogement.objects.get(id=pk)
    thisId = deletedImage.annonce.id
    deletedImage.delete()
    return HttpResponseRedirect(reverse("dashboard-image", args=[thisId]))

@login_required
def calendrier(request, pk):
    myObject = Annonce.objects.get(id=pk)
    calendriers = Calendrier.objects.filter(annonce=myObject)
    context={'obj':myObject, 'calendrier': calendriers}
    return render(request,'annonce/dashboard/calendrier.html',context)

@login_required
def create_calendrier(request,pk):
    annonce = Annonce.objects.get(id=pk)
    debut = request.POST.get('calendrier_debut')
    fin = request.POST.get('calendrier_fin')
    disponibilite = request.POST.get('disponibilite')
    if request.method=='POST':
        calendrier = Calendrier.objects.create(
            annonce=annonce,
            calendrier_debut=debut,
            calendrier_fin=fin,
            disponibilite=disponibilite,
        )
        calendrier.save()
        return HttpResponseRedirect(reverse("dashboard-calendrier", args=[annonce.id]))
    context = {'annonce' : annonce}
    return render(request,'annonce/dashboard/create-calendrier.html',context)

@login_required
def edit_calendrier(request, pk):
    calendrier = Calendrier.objects.get(id=pk)
    annonce = calendrier.annonce
    debut = request.POST.get('calendrier_debut')
    fin = request.POST.get('calendrier_fin')
    disponibilite = request.POST.get('disponibilite')
    if request.method == 'POST':
        calendrier.calendrier_debut = debut
        calendrier.calendrier_fin = fin
        calendrier.disponibilite = disponibilite
        calendrier.annonce = annonce
        calendrier.save()
        return HttpResponseRedirect(reverse("dashboard-calendrier", args=[annonce.id]))
    context = {'annonce': annonce, 'calendrier': calendrier}
    return render(request, 'annonce/dashboard/create-calendrier.html', context)

@login_required
def condition_view(request, pk):
    form = FormCondition()
    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    myCondition = Condition.objects.get(annonce=myObject)
    if request.method =='POST':
        form = FormCondition(request.POST, instance=myCondition)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = FormCondition(instance=myCondition)
    context = {'form': form, 'obj': myObject, 'requete': requete}
    return render(request,'annonce/dashboard/conditions.html',context)

def diagnsotic_view(request, pk):
    form = FormDiagnostic()
    requete = request.user
    myObject = Annonce.objects.get(id=pk)
    myDiagnostic = Diagnostic.objects.get(annonce=myObject)
    if request.method =='POST':
        form = FormDiagnostic(request.POST, instance=myDiagnostic)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = FormDiagnostic(instance=myDiagnostic)
    context = {'form': form, 'obj': myObject, 'requete': requete}
    return render(request,'annonce/dashboard/diagnostic.html',context)

@login_required()
def user_view_dashboard(request, pk):

    myObject = Annonce.objects.get(id=pk)
    user = request.user
    form = UserModif(instance=user)
    rue = request.POST.get('rue')
    voie = request.POST.get('voie')
    ville = request.POST.get('ville')
    region = request.POST.get('region')
    zip = request.POST.get('zip')
    pays = request.POST.get('pays')
    myAdress = Address.objects.get(account=user)

    if request.method == 'POST':
        form = UserModif(request.POST, instance=user)
        if form.is_valid():
            myAdress.rue = rue
            myAdress.voie = voie
            myAdress.ville = ville
            myAdress.region = region
            myAdress.zipCode = zip
            myAdress.pays = pays
            myAdress.save()
            user = form.save()
            form.save()
            return redirect('/')
    else:
        form = UserModif(instance=user)

    context = {'form': form, 'obj': myObject, 'address': myAdress}

    return render(request,'annonce/dashboard/userDashboard.html',context)

def verification_view(request, pk):
    myObject = Annonce.objects.get(id=pk)
    user = request.user
    form = VerifImage(instance=user)
    if request.method =='POST':
        form = VerifImage(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        form = VerifImage(instance=user)
    context = {'form': form, 'obj': myObject, 'user': user,}

    return render(request,'annonce/dashboard/verif.html',context)
