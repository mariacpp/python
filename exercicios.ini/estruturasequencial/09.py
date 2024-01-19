#TODO: Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

f = float(input('digite a temperatura em graus Fahrenheint: '))

c = 5 * ((f-32)/9)

print(f'A temperatura em graus Celsius é de {c:.2f}°C.')