while True:
    try: # tratamento de erros
        n = int(input("Entre com um número: "))
    except ValueError as erro: #exeção
        print('O valor informado não é um número!')
        print(erro)
    