from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils.baseconv import base64
from django.views import View

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.core.mail import EmailMessage

# Create your views here.
def streaming_index(request):
    context = {}
    return render(request, 'blog.html', context)