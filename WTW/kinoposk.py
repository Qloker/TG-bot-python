import requests
import json

url = 'https://api.kinopoisk.dev/v1/movie/random'
API_KEY = 'HKZ4SGG-YPCMWDK-NDCEZ9M-T4FR0MR'

headers = {'accept': 'application/json', 'X-API-KEY': API_KEY}

params = {'keyword'}

repsonse = requests.get(url=url, headers=headers)

if repsonse.status_code == 200:
    data = repsonse.json()
    print(data['name'])
else:
    print(repsonse.status_code)