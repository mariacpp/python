'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

peso = float(input('digite o peso de peixes pescados: '))
if peso>50:
    exc = peso - 50

multa = exc * 4.00

print(f'\no peso que você trouxe foi {peso} Kg,\no excesso foi de {exc} Kg e o total a pagar de multa é de R${multa}')