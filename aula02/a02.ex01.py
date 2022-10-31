c = 's'
while c == 's' or c == 'sim':

    try:
        peso = float(input('Digite o peso: '))
    except:
        print('Valor do tipo incorreto foi informado!')
    try:
        altura = float(input('Digite a altura: '))
    except:
        print('Valor do tipo incorreto foi informado!')
    
    imc = peso / (altura**2)
    print('O imc é ', imc)
    c = str(input('Deseja continuar? s/n \n')).lower()

