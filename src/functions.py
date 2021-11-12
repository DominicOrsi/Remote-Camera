import requests
import json
import time
import config

# Main URL
# Needed for every function

main_url = config.PROTOCOL + config.IP_ADDRESS + ":" + config.PORT + "/" + "ccapi/" + config.VERSION

'''
CAMERA STATUS (Variable Values)

'''

def storageInfo():
    storage_url = main_url + "/devicestatus/storage"
    storage_response = requests.get(storage_url)
    storage_dic = json.loads(storage_response.text)
    storage_list = storage_dic["storagelist"]
    print("Name:", storage_list[0]["name"])
    print("Card size:", round(storage_list[0]["maxsize"] / 1073741824, 2), "gb")
    print("Space avalible:", round(storage_list[0]["spacesize"] / 1073741824, 2), "gb")
    print("Images on card:", storage_list[0]["contentsnumber"])

def batteryInfo():
    # Battery stuff
    battery_url = main_url + "/devicestatus/battery"
    battery_response = requests.get(battery_url)
    battery_dic = json.loads(battery_response.text)
    print("Name:", battery_dic["name"])
    print("Kind:", battery_dic["kind"])
    print("Level:", battery_dic["level"])
    print("Quality:", battery_dic["quality"])

def checkLens():
    lens_url = main_url + "/devicestatus/lens"
    lens_response = requests.get(lens_url)
    lens_dic = json.loads(lens_response.text)
    print("Lens info:", lens_dic["name"])
    

'''
SHOOTING AND RECORDING

'''

# Sending the request to take a still photo
def shootingStill():
    shooting_url = main_url + "/shooting/control/shutterbutton"
    shooting_response = requests.post(shooting_url, json={"af": config.AUTOFOCUS})
    print("\nPhoto taken")
    print("Status code:", shooting_response.status_code)
    print("Entire Post Response")
    print(shooting_response.json)

# Sending request to for recording
def recordButton(length):
    # Calls movie mode to enable recording
    movieMode("on")
    record_url = main_url + "/shooting/control/recbutton"
    record_response = requests.post(record_url, json={"action": "start"})
    print("\nRecord request started")
    print("Status code:", record_response.status_code)
    print(record_response.text)
    time.sleep(length) # The parameter passed in goes here for how long to record for
    record_response = requests.post(record_url, json={"action": "stop"})
    movieMode("off")
    print("\nRecord request ended")
    print("Status code:", record_response.status_code)
    print("Entire Post Response")
    print(record_response.text)

def movieMode(status):
    movie_url = main_url + "/shooting/control/moviemode"
    movie_response = requests.post(movie_url, json={"action": status})
    print("\nMoive mode set", status)
    print("Status code:", movie_response.status_code)

def changeISO(iso):
    # Changing ISO
    iso_url = main_url +"/shooting/settings/iso"
    iso_response = requests.put(iso_url, json={"value": iso})
    print("\nStatus code:", iso_response.status_code)
    print("Entire Post Response")
    print(iso_response.json)


def lensZoom():
    lens_url = main_url + "/shooting/control/zoom"
    lens_response = requests.get(lens_url)
    print(lens_response.text)


'''
IMAGE PROCESSING
'''

# Image processing imports
from PIL import Image
from io import BytesIO

def liveView():
    live_url =  main_url + "/shooting/liveview"
    # print(live_url)
    live_response = requests.post(live_url, json={"liveviewsize": "small", "cameradisplay": "on"})
    print("\nStatus code:", live_response.status_code)
    print("Entire Post Response\n", live_response.json)

def flipLive():
    flip_url = main_url + "/shooting/liveview/flip"
    flip_response = requests.get(flip_url)
    e = Image.open(BytesIO(flip_response.content))
    print(flip_response.json)