import requests
import json
import time

main_url = "http://147.222.70.18:8080/ccapi/ver100"


def battery():
    # Battery stuff
    battery_url = main_url + "/devicestatus/battery"
    battery_request = requests.get(battery_url)
    battery_dic = battery_request.text
    battery_dic = json.loads(battery_dic)
    print("Name:", battery_dic["name"])
    print("Kind:", battery_dic["kind"])
    print("Level:", battery_dic["level"])
    print("Quality:", battery_dic["quality"])

# Sending the request to take a still photo
def shootingStill():
    shooting_url = main_url + "/shooting/control/shutterbutton"
    shooting_response = requests.post(shooting_url, json={"af": True})
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

def changeISO():
    # Changing ISO
    iso_url = main_url +"/shooting/settings/iso"
    iso_response = requests.put(iso_url, json={"value": "8000"})
    print("\nStatus code:", iso_response.status_code)
    print("Entire Post Response")
    print(iso_response.json)

def checkLens():
    lens_url = main_url + "/devicestatus/lens"
    lens_response = requests.get(lens_url)
    print(lens_response.text)

def lensZoom():
    lens_url = main_url + "/shooting/control/zoom"
    lens_response = requests.get(lens_url)
    print(lens_response.text)