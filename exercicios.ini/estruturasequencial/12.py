#TODO: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

a = float(input('digite sua altura (ex: m.cm): '))
pi =(72.7*a) - 58

print(f'o peso ideal é {pi:.2f} kg')