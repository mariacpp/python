f = open("aula04/exercicios/arquivo.txt", "r")
linhas = f.readlines()

f2 = open("aula04/exercicios/outroarq.txt", "w")

f2.writelines(linhas)

f.close()
f2.close()

f2 = open("aula04/exercicios/outroarq.txt", "r")
print(f2.read())

f2.close()