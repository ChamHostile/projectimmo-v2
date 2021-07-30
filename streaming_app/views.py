from django.shortcuts import render
import requests

# Create your views here.
from django.conf import settings

def streaming_index(request):
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

    # Create a video container
    payload2 = {
        "title": "Demo Vid from my Computer",
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
    file = {"file": open("/home/zaza/Téléchargements/pexels-rodnae-productions-6691597.mp4", "rb")}

    response = requests.request("POST", upload_url, files=file, headers=headers_upload)
    json_response = response.json()
    print(json_response)

    context = {'response2': response2}
    return render(request, 'blog.html', context)