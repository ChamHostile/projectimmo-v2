
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm, FileInput
from django import forms

from .models import *
from account.models import Account
from crispy_forms.helper import FormHelper


class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ["name"]
		widgets = {
			"name": FileInput(attrs={'multiple': True})
		}

class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('email','first_name','last_name','telephone', 'packages_type')
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
