import network
import socket
from time import sleep
import machine
import os
import urequests
setupssid = input("Enter WLAN/Wi-Fi SSID: ")
setuppassword = input("Enter WLAN/Wi-Fi password: ")
setupurl = 'https://raw.githubusercontent.com/Beguwula/PicoDownloader/main/downloader.py'
setupfilename = 'downloader.py'
def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
def download(url, filename):
    path = filename
    response = urequests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"File saved as {path}")
    else:
        print(f"Error downloading file from {url}")
connect(setupssid, setuppassword)
download(setupurl, setupfilename)
del network
del socket
del sleep
del machine
del os
del urequests
del setupssid
del setuppassword
del setupurl
del setupfilename
del connect
del download
