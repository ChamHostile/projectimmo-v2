from django.forms import ModelForm
from .models import Annonce
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from address.forms import AddressField
from account.models import Account
from crispy_forms.helper import FormHelper

class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        exclude = ['user']
        helper = FormHelper()

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('email','first_name','last_name','telephone','typelocataire')
        helper = FormHelper()
