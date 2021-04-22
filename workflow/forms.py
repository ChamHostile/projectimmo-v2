from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import File
from django.forms import ModelForm
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from address.forms import AddressField
from crispy_forms.helper import FormHelper
from functools import partial


class NewFile(ModelForm):
    class Meta:
        model = File
        exclude = ['address', 'verdict']
        widgets = {
            'type_visite': forms.RadioSelect()
        }
        def __init__(self, *args, **kwargs):
            super(NewFile, self).__init__(*args,**kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class UpdateFile(ModelForm):
    class Meta:
        model = File
        fields = ['verdict']






