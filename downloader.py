import network
import socket
from time import sleep
import machine
import os
import urequests
def connect(ssid):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
def download(url, filename):
    path = filename
    response = urequests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"File saved as {path}")
    else:
        print(f"Error downloading file from {url}")
