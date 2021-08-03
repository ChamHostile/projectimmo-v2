from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm
from django import forms

from .models import *

class VideoForm(ModelForm):
	class Meta:
		model = Video
		fields = '__all__'
