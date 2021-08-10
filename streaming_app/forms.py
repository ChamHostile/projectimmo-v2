
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm, FileInput
from django import forms

from .models import *

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ["name"]
		widgets = {
			"name": FileInput(attrs={'multiple': True})
		}
