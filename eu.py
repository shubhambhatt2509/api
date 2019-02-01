import requests
import json

r = requests.get('https://restcountries.eu/rest/v2/region/europe')
for a in r.json():
    r=a['regionalBlocs']
    for i in ['regionalBlocs']:
      print(a['name']) 