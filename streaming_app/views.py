import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
import requests
from django.templatetags.static import static
# Create your views here.
from django.conf import settings
from django.urls import reverse

from .forms import VideoForm
from .models import Video
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def streaming_page(request):
    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("streaming_index")
    else:
        form = VideoForm()
    context = {'form':form}
    return render(request, 'blog.html', context)

def streaming_index(request):
    video = Video.objects.latest('id')
    auth_url = "https://ws.api.video/auth/api-key"
    create_url = "https://ws.api.video/videos"
    headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
    }

    payload = {
            "apiKey": "w2tWDSCvelfM16lqyPVyAxMs5uAY2G7oAbxPud656qO"
        }
    response = requests.request("POST", auth_url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")

    auth_string = "Bearer " + token
        # Set up headers for authentication
    headers_bearer = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_string
    }
    titre = video.name.name
    # Create a video container
    payload2 = {
        "title": "Video_test",
        "description": "Video upload of Big Buck Bunny to demo how to do an upload from a folder on your computer."
    }

    response = requests.request("POST", create_url, json=payload2, headers=headers_bearer)
    response = response.json()
    response2 = response
    videoId = response["videoId"]

    upload_url = create_url + "/" + videoId + "/source"

    headers_upload = {
            "Accept": "application/vnd.api.video+json",
            "Authorization": auth_string
    }
    video_url = video.name.path
    file = {"file": open(video_url, "rb")}

    response = requests.request("POST", upload_url, files=file, headers=headers_upload)
    json_response = response.json()
    print(json_response)

    return HttpResponse(response)