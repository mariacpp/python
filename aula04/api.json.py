import requests
import json


navegador = {
    "User-Agent" : "Chrome"
}

data = requests.get(url='https://parallelum.com.br/fipe/api/v1/carros/marcas',headers=navegador)

for marca in data.json():
    for k, v in marca.items():
        print(f"{k}: {v}")
    print()
