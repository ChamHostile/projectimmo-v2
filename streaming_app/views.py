import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
import ffmpeg

from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user

BASE_DIR = Path(__file__).resolve().parent.parent


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('streaming_page')

    context = {}
    return render(request, 'compte/login-annonce.html')

@login_required
def logout_streaming(request):
    logout(request)
    return redirect('stream_main')


@login_required(login_url='login-stream')
def streaming_page(request):
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
    querystring = {"currentPage": "1", "pageSize": "25"}

    response2 = requests.get(create_url, headers=headers_bearer, params=querystring)
    response2 = response2.json()
    data = response2["data"]
    user_video = Video.objects.filter(user=request.user)
    video_length = 0
    for video in data:
        video_length += 1
    length_loop = video_length - 6
    print(length_loop)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        files = request.FILES.getlist('video_upload')
        title = request.POST.get('file_name')
        length = int(len(files))
        if form.is_valid():
            for f in files:
                video = Video.objects.create(name=f, file_name=title, user=request.user)
                video.save()
            return redirect("streaming_index", pk=length)
    else:
        print("no post")
    context = {'response': data, 'length': length_loop, 'user_video': user_video}
    return render(request, 'streaming/tmart/product-details.html', context)

def stream_main(request):
    context = {}
    return render(request, 'streaming/tmart/shop.html', context)

def streaming_plateform(request):
    url = "https://ws.api.video/auth/api-key"

    payload = {"apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")

    url = "https://ws.api.video/live-streams"

    payload = {
        "record": False,
        "name": "Bob"
    }
    headers = {
        "Accept": "application/vnd.api.video+json",
        "Content-Type": "application/json",
        "Authorization": token
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()

    stream_key = response.get("streamKey")
    iframe = response["assets"]["iframe"]
    player = response["assets"]["player"]
    print("iFrame :", iframe)
    print("player :", player)
    print("streamkey: ", stream_key)
    rtmp_url = "rtmp://broadcast.api.video/s/" + stream_key
    return redirect('live_stream', rtmp_url=str(rtmp_url), player=str(player))

def streaming_index(request, pk):
    video = Video.objects.all().order_by('-id')[:pk]
    i = 0
    for myupload in video:
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
        titre = myupload.file_name
        # Create a video container
        payload2 = {
            "title": titre,
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
        video_url = myupload.name.path
        file = {"file": open(video_url, "rb")}

        response = requests.request("POST", upload_url, files=file, headers=headers_upload)
        json_response = response.json()
        print(json_response)

        return redirect(streaming_page)


def live_stream(request, rtmp_url, player):
    (
        ffmpeg
            .input('/dev/video0', format='video4linux2', framerate=25)
            .output(rtmp_url, format='flv', flvflags='no_duration_filesize')
            .run_async()
    )
    context = {'player':player}
    return render(request, 'annonce.html', context)

