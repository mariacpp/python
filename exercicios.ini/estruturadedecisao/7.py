'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = float(input('digite um número: '))
n2 = float(input('digite outro número: '))
n3 = float(input('digite mais um número: '))

if n1 > n2 and n1>n3 and n2<n3:
    print(f'maior: {n1}\nmenor: {n2}')
if n1 > n2 and n1>n3 and n3<n2:
    print(f'maior: {n1}\nmenor: {n3}')
elif n2>n1 and n2>n3 and n1<n3:
    print(f'maior: {n2}\nmenor: {n1}')
elif n2>n1 and n2>n3 and n3<n1:
    print(f'maior: {n2}\nmenor: {n3}')
elif n3>n1 and n3>n2 and n1<n2:
    print(f'maior: {n3}\nmenor: {n1}')
elif n3>n1 and n3>n2 and n2<n1:
    print(f'maior: {n3}\nmenor: {n2}')