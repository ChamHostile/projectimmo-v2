from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from address.forms import AddressField
from account.models import Account
from crispy_forms.helper import FormHelper
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AnnonceForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['address','categorie_logement', 'type_location_choices']
        def __init__(self, *args, **kwargs):
            super(AnnonceForm, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class LoggedForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['address','categorie_logement', 'type_location_choices']
        def __init__(self, *args, **kwargs):
            super(AnnonceForm, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('email','first_name','last_name','telephone','typelocataire')
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class DescriptionForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre_logement','address','description','categorie_logement','nombre_personne', 'pieces_couchage']
        def __init__(self, *args, **kwargs):
            super(DescriptionForm, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class EquipmentForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['equipements']
        def __init__(self, *args, **kwargs):
            super(EquipmentForm, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class EquipmentForm(ModelForm):
    class Meta:
        model = Annonce
        fields = ['equipements']
        def __init__(self, *args, **kwargs):
            super(EquipmentForm, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class FormLoyer(ModelForm):
    class Meta:
        model = Annonce
        fields = ['loyer_tc', 'charges_loyer']
        def __init__(self, *args, **kwargs):
            super(FormLoyer, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class FormCalendrier(ModelForm):
    class Meta:
        model = Calendrier
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(FormCalendrier, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'