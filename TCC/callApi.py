import json 
import requests

api_url = 'http://127.0.0.1:5000/api/v1/resources/disponibilidade/verifica'
send = [332373,208,11,212,7,14,4,20,34,8,3,1,4,200]
r = requests.post(url = api_url, json=send)

print(r.text)