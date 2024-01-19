'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''
l = input('digite uma letra: ')

if l.lower() in 'aeiou':
    print(f'{l} é uma vogal.')
else:
    print(f'{l} é uma consoante')