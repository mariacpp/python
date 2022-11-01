import psycopg2 as pg

try:
    con = pg.connect(
        database="projeto",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("conexão realizada")
    con.close()
except Exception as erro:
    print(erro)


def Menu():
    print("1 - entrar\n")
    print("2 - cadastrar")
    op = int(input("digite sua opção: "))


def Cadastrar():
    nome = input("digite o seu nome: ")
    email = input("digite o seu email: ")
    user = input("digite seu usuário: ")
    dtnsc = input("digite sua data de nascimento (dd-mm-aaaa): ")
    senha = input("defina sua senha: ")

def Login():
    user = input("digite seu usuário: ")
    senha = input("digite sua senha: ")
    #if para checar user e senha se True: print("Seja-bem vindo(a)")
