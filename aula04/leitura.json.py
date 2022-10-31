import json

data = {}

data["sp"] = "São Paulo"
data["rj"] = "Rio de Janeiro"
data["mg"] = "Minas Gerais"

f = open("aula04/output.json","w")
json.dump(data,f,sort_keys=True,indent=4)
f.close()

f = open("aula04/output.json","r")
data = json.load(f)
f.close()

print(data)