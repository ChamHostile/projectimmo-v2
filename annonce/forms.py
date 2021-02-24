from django.forms import ModelForm
from .models import Annonce
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from address.forms import AddressField
from account.models import Account
class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('email','first_name','last_name','telephone','typelocataire')
