import requests
import pandas as pd
import json

main_url = "http://147.222.70.18:8080/ccapi/ver100"


# Battery stuff
battery_url = main_url + "/devicestatus/battery"
battery_request = requests.get(battery_url)
battery_dic = battery_request.text


battery_dic = json.loads(battery_dic)
print("Level:", battery_dic["level"])

# Shooting request
shooting_url = main_url + "/shooting/control/shutterbutton"
shooting_response = requests.post(shooting_url, json={"af": True})
print("\nStatus code:", shooting_response.status_code)
print("Entire Post Response")
print(shooting_response.json)

