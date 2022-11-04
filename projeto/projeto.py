import psycopg2 as pg

#CONECTAR NO BD
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

#CRIAR TABLES
def CriarTables():
    cur = con.cursor()
    cur.execute("CREATE TABLE USUARIOS (id serial PRIMARY KEY, email varchar, senha varchar)")
    cur.execute("CREATE TABLE LIVROS(id serial PRIMARY KEY, titulo varchar, autor varchar, ano integer, editora varchar, quantidade integer)")
    cur.execute("CREATE TABLE EMPRESTIMO(id serial PRIMARY KEY, nome varchar, CPF varchar unique, titulo VARCHAR, FOREIGN KEY(titulo) REFERENCES LIVROS(titulo))")  

    
def Main():
    print("-=-=-=-=-=-=-=-=-INICIO-=-=-=-=-=-=-=-=-\n")
    print("1 - entrar\n")
    print("2 - cadastrar\n")
    print("3 - sobre\n")
    Iop = int(input("digite sua opção: "))
    if Iop == 1:
        Login()
    if Iop == 2:
        Cadastrar()
    if Iop == 3:
        Sobre()


def Sobre():
    print("=-=-=-=-=-=-=-=-=SOBRE=-=-=-=-=-=-=-=-=\n")
    print('''Gerenciador de acervo de biblioteca. 
Com esse projeto podemos cadastrar livros, 
lugar, devolver e exportar dados do acervo. 
    ''')


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


def Menu():
    print('''
            1 - Alugar livro\n
            2 - Devolver livro\n
            3 - Consultar títulos\n
            4 - Cadastrar livro\n
            5 - Relatório\n
            6 - Sair\n
             ''')
    Mop = int(input('digite sua opção: '))


Main()