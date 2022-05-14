# este archivo importara JSON 

import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/albums')
exportado = response.json()
for item in exportado :
    print(item["id"], item["title"])
    print(item.keys())