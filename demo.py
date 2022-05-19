#pour test Api get
import json
import requests

api_lien = "http://127.0.0.1:5000/get-fruit"

json = requests.get(api_lien).json()

JSON = json['fruit']

print(JSON)

#ne pas oublier de faire  python3 demo.py dans le terminal  