import requests
import json

tipo = str(input('Qual o tipo de veiculo?\n'))
ano = str(input('Qual o ano do veiculo? [ano-mês] \n'))
codfp = str(input('Qual o código fipe do veiculo?\n'))

navegador = {
    "User-Agent" : "Chrome"
}

url = f'http://parallelum.com.br/fipe/api/v2/{tipo}/{codfp}/years/{ano}/history'

r = requests.get(url=url)

print(r)
'''for marca in data.json():
    for k, v in marca.items():
        print(f"{k}: {v}")
    print()'''