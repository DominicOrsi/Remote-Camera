import requests
import pandas as pd
import json


url = "http://147.222.70.18:8080/ccapi/ver100/devicestatus/battery"

r = requests.get(url)

battery_df = r.text

for i in battery_df:
    print(i)

print(battery_df)
print(r)