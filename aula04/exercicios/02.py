f = open("aula04/exercicios/arquivo.txt", "r")
linhas = f.readlines()

l = []

for linha in linhas:
    l.append(linha)

print(l)

f.close()