import os

'''def nome_funcao(arg1,arg2,...,argn):
    #bloco de código
    return valor_retorno(opcional)'''

def LimparTela():
    os.system('cls')
        
def ler_numero():
    return int(input('Informe um valor> '))

def soma(n1,n2):
    return n1+n2

def main():
    LimparTela()
    n1 = ler_numero()
    n2 = ler_numero()
    print(soma(n1, n2))
    
main()

