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
from .forms import CreateUserForm
from .models import Video
from django.conf import settings
from pathlib import Path
from account.models import Account
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
    return render(request, 'compte/login-stream.html')

@unauthenticated_user
def register_streaming(request, pk):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        package = request.POST.get('packages_type')
        if form.is_valid():
                user=form.save(commit=False)
                user.packages_type = package
                user.is_active = True
                user.save()
                new_user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password1'],)
                if user is not None:
                    login(request, new_user)
                    return redirect('profil-stream')
    context={'form':form, 'id': pk}
    return render(request,'compte/inscription_stream.html',context)

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
        "apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"
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
    url = "https://ws.api.video/auth/api-key"

    payload = {"apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")

    auth_string = "Bearer " + token
    # Set up headers for authentication
    headers_bearer = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_string
    }
    url = "https://ws.api.video/videos"

    response = requests.request("GET", url, headers=headers_bearer)
    response = response.json()
    data = response["data"]
    this_url = 'videos'
    context = {'response': data, 'url': this_url}
    return render(request, 'streaming/tmart/shop.html', context)

def live_main(request):
    url = "https://ws.api.video/auth/api-key"

    payload = {"apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")

    auth_string = "Bearer " + token
    # Set up headers for authentication
    headers_bearer = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": auth_string
    }
    url = "https://ws.api.video/live-streams"

    response = requests.request("GET", url, headers=headers_bearer)
    response = response.json()
    data = response["data"]
    this_url = 'live-streams'
    context = {'response': data, 'url': this_url}
    return render(request, 'streaming/tmart/shop.html', context)

def streaming_plateform(request):

    if request.method == 'POST':
        titre = request.POST.get('titre')
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
            "name": titre
        }
        headers = {
            "Accept": "application/vnd.api.video+json",
            "Content-Type": "application/json",
            "Authorization": token
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        response = response.json()
        id = response.get("liveStreamId")

        return redirect('live_stream', id=id)

    context = {}
    return render(request, 'streaming/tmart/checkout.html', context)

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
            "apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"
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
            "description": "Video upload of Big Buck Bunny to demo how to do an upload from a folder on your computer.",

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


def live_stream(request, id):
    url = "https://ws.api.video/auth/api-key"

    payload = {"apiKey": "WdPYsqTeTFnUe1MqklfqsOOwDZdyFAzJl5FAt6RDd9h"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.json()
    token = response.get("access_token")

    url = "https://ws.api.video/live-streams/{}".format(id)

    headers = {
        "Accept": "application/json",
        "Authorization": token
    }

    response = requests.request("GET", url, json=payload, headers=headers)
    response = response.json()

    stream_key = response.get("streamKey")
    iframe = response["assets"]["iframe"]
    player = response["assets"]["player"]
    print("iFrame :", iframe)
    print("player :", player)
    print("streamkey: ", stream_key)
    rtmp_url = "rtmp://broadcast.api.video/s/" + stream_key
    (
        ffmpeg
            .input('/dev/video0', format='video4linux2', framerate=25)
            .output(rtmp_url, format='flv', flvflags='no_duration_filesize')
            .run_async()
    )

    context = {'player':player, 'response': response}
    return render(request, 'streaming/tmart/customer-review.html', context)

def profil_stream(request):
    context = {}
    return render(request, 'compte/profile_stream.html')
