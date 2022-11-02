from sys import api_version
from urllib import request
import requests

latitud = 19.236169
longitud = -98.9521357

api_key= "3002b12019148b8334512dd25346f0e9"

url_destino = "http://api.openweathermap.org/data/2.5/weather?q=Mexico,mx&APPID=3002b12019148b8334512dd25346f0e9" #f"http://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&lang=es&APPID={api_version}"

respuesta = requests.get(url_destino)

if respuesta.status_code != 200:
    print("Ha ocurrido un error. Intente nuevamente.")
    exit()

datos = respuesta.json()
ciudad = datos["name"]

datos_clima=datos["weather"]
clima = datos_clima[0]["description"]

print(f"El clima en la ciudad {ciudad} es {clima}")