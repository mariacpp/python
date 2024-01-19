'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = input('digite uma letra (ex: \'F\' ou \'M\'): ')

if letra.upper() == 'M':
    print('M - masculino')
elif letra.upper() == 'F':
    print('F - feminino')
else:
    print('sexo invalido')