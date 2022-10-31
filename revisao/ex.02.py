import random

i = int(input("digite o número de linhas: "))
j = int(input("digite o número de colunas: "))

array = []
arr = []
for l in range(0,i):
    for c in range(0,j):
        num = random.randint(0, 10)
        arr.append(num)
    array.append(arr[:])
    arr.clear()

print(array)
