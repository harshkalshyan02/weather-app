import os
import requests
import json
city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=e885e20a8d2945309a181338241903&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
lu = wdic["current"]["last_updated"]
wkph = wdic["current"]["wind_kph"]
fl = wdic["current"]["feelslike_c"]
os.system(f"say 'The current weather in {city} which is last updated on {lu} is {w} degrees, wind speed is {wkph}. Temperature feels like {fl} degrees'")
