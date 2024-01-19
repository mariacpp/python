'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato'''

p1 = float(input('digite o preço do produto 1: '))
p2 = float(input('digite o preço do produto 2: '))
p3 = float(input('digite o preço do produto 3: '))

if p1<p2 and p1<p3:
    print(f'compre o produto 1')
if p2<p1 and p2<p3:
    print(f'compre o produto 2')
if p3<p2 and p3<p1:
    print(f'compre o produto 3')
