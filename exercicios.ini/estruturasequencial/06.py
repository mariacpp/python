#TODO: Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

r = float(input('digite o raio do circulo: '))
pi = math.pi

area = pi * (r**2)

print(f'A = {pi}*{r}² = {area}')
