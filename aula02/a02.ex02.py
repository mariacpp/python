pares =[]
impares = []
def receber(*num):
    for n in num:
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
            

def resultado(pares, impares, nmrs):
    print()
    print('-------------RESULTADO--------------')
    print('Quantidade de pares: ', len(pares))
    print('Números impares: ', impares)
    print('Maior número: ', max(nmrs))
    print('Média: ', sum(nmrs)/len(nmrs))
    print('------------------------------------')          
    
c = 's'
nmrs = []
while c == 's' or c =='sim':
    num = int(input('Digite o numero: '))
    nmrs.append(num)
    receber(num)
    c = str(input('Deseja continuar? s/n \n')).lower()
    

resultado(pares, impares, nmrs)