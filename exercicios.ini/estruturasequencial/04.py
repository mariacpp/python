#TODO: Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n = [] # or n = list()

for i in range(1,5):
    num = float(input(f'digite a nota {i}...: '))
    n.append(num)

print(n)
soma = sum(n)
media = soma/len(n)

l = 0
for i in n:
    l = l+ 1
    if l < 4:
        print(f'{i} + ', end='')
    else:
        print(f'{i}', end='')


print(f'/{len(n)} = {media}')
