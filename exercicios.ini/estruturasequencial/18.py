'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

'''t = A/V'''

a = float(input('digite o tamanho do arquivo em MB: '))
v = float(input('digite a velocidade do link de internet em Mbps: '))
t = a/v

print(f'o tempo aproximado de download é de {t:.2f} segundos')