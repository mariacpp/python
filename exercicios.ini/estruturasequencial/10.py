#TODO: Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

#F = (C × 9/5) + 32

c = float(input('digite a temperatura em Celsius: '))

f = (c * 9/5) + 32

print(f'a temperatura em Fahrenheit é de {f:.2f}°F')