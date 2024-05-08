import requests
import os


url = "https://api.rawg.io/api/games"
key=os.environ["key"]

params = {
    "key": key,
    "search": "God of War",
    "page_size": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error al realizar la solicitud:", response.status_code)

