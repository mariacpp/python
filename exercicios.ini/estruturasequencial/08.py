#TODO: Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
vl = float(input('quanto vc ganha por hora? resp: '))
hr = float(input('quantas horas vc trabalhou no mês? resp: '))

sal = vl * hr

print(f'O valor do seu salário no mês é R${sal}.')