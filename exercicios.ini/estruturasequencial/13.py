#TODO: tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h = float(input('digite sua altura: '))
s = input('digite seu genero (F/M): ').upper()

if s == 'M':
    pi = (12.7 * h) - 58
elif s == 'F':
    pi = (62.1*h) - 44.7
else:
    print('opção invalida')

print(f'o peso ideal é {pi:.2f} Kg')