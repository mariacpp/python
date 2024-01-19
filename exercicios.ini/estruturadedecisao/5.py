'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
n1 = float(input('digite a nota parcial 1: '))
n2 = float(input('digite a nota parcial 2: '))

media = (n1+n2)/2

if media>=7 and media <10:
    print(f'média: {media} - Aprovado!')
elif media < 7:
    print(f'média: {media} - Reprovado!')
elif media ==10:
    print(f'média: {media} - Aprovado com Distinção!') 