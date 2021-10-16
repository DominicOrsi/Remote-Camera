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
    print("Level:", battery_dic["level"])

# Sending the request to take a still photo
def shootingStill():
    shooting_url = main_url + "/shooting/control/shutterbutton"
    shooting_response = requests.post(shooting_url, json={"af": True})
    print("\nStatus code:", shooting_response.status_code)
    print("Entire Post Response")
    print(shooting_response.json)

# Sending request to for recording
def movieRecord(sleep):
    movie_url = main_url + "/shooting/control/moviemode"
    movie_response = requests.post(movie_url, json={"action": "on"})
    print("\nMovie request started")
    print("Status code:", movie_response.status_code)
    time.sleep(sleep)
    movie_response = requests.post(movie_url, json={"action": "off"})
    print("\nMovie request started")
    print("Status code:", movie_response.status_code)
    print("Entinre Post Response")
    print(movie_response.json)


def changeISO():
    # Changing ISO
    iso_url = main_url +"/shooting/settings/iso"
    iso_response = requests.put(iso_url, json={"value": "8000"})
    print("\nStatus code:", iso_response.status_code)
    print("Entire Post Response")
    print(iso_response.json)
