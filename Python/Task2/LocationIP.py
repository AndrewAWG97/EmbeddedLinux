#!/bin/python3

import requests

resp = requests.get("https://api.ipify.org/?format=json")
dic = resp.json()
ip = dic["ip"]

resp = requests.get(f"https://ipinfo.io/{ip}/geo")
location = resp.json()

print(f"Location data for IP {ip}:")
print(f"City: {location.get('city')}")
print(f"Region: {location.get('region')}")
print(f"Country: {location.get('country')}")
print(f"Location: {location.get('loc')}")

