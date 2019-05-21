import base64
import json
import requests
import sys
import subprocess
import time
import signal
from base64 import b64encode

client_id = 'client_id'
headers = {"Authorization": "Client-ID client_id"}
api_key = 'api_key'
url = "https://api.imgur.com/3/upload.json"
j1 = requests.post(
    url,
    headers = headers,
    data = {
        'key': api_key,
        'image': b64encode(open('1.jpg', 'rb').read()),
        'type': 'base64',
        'name': '1.jpg',
        'title': 'p1'
    }
)
link = j1.json()["data"]["link"]

subprocess.Popen(["mosquitto_pub", "-h", "beam.soracom.io", "-p", "1883", "-t", "image", "-m", link], stdout=subprocess.PIPE)
