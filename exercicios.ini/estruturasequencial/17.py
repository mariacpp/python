'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

import math


a = float(input('digite o tamanho da área em metros quadrados: '))
tp = input('o tipo de compra vai ser em: \n(L) Latas\n(G) Galões\n(M)Misturado\ndigite o tipo: ')
litros = a/6
plt = 80
pgl = 25
if tp.upper() == 'L':
    latas = litros/18
    pt = math.ceil(latas) * plt
    print(f'a quantidade de latas a serem compradas é de: {math.ceil(latas)} e o valor a ser pago é de R${pt}')

elif tp.upper() == 'G':
    galoes = litros/3.6
    pt = math.ceil(galoes) * pgl
    print(f'a quantidade de galões a serem compradas é de: {math.ceil(galoes)} e o valor a ser pago é de R${pt}')

elif tp.upper() == 'M':
        litros = litros + (litros * (10/100))
        latas = litros/18
        resto = litros//18
        galoes = resto/3.6
        latas = math.ceil(latas)
        galoes = math.ceil(galoes)
        pt = latas * plt + galoes * pgl
        print(f'a quantidade de latas a seres compradas é de: {latas}\nquantidade de galões a serem compradas é de: {galoes}\n e o valor a ser pago é de R${pt}')
        

    

