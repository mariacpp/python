'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
import math
a = float(input('digite o tamanho em m² da área a ser pintada: '))
litros = a/3
latas = litros/18
pt = math.ceil(latas) * 80

print(f'a quantidade de latas a serem compradas é de: {math.ceil(latas)} e o valor a ser pago é de R${pt}')
