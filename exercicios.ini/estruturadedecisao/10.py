'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''


t = input('(M) matutuno \n(V) vespertino \n(N) noturno \ndigite o turno em que vc estuda: ').upper()

if t == 'M':
    print('Bom dia!')
elif t =='V':
    print('Boa tarde!')
elif t == 'N':
    print('Boa noite!')
else:
    print('Valor invalido!')