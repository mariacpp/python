import psycopg2 as pg
import maskpass as mask


def GravarLivros():
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        print("conexão realizada")
        try:
            cur = con.cursor()    
            script = """INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('A Guerra dos tronos', 'George R.R. Martin', 2019, 'Suma', 'no');
            INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('A Furia dos reis', 'George R.R. Martin', 2019, 'Suma', 'yes');
            INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('A Tormenta das espadas', 'George R.R. Martin', 2019, 'Suma', 'no');"""
            try:
                cur.execute(script)
                print("Livros cadastrados.\n")
            except Exception as erro:
                print(erro)
            con.commit()
            con.close()
        except Exception as error:
            print(error)    
    except Exception as erro:
        print(erro)

#CRIAR TABLES
def CriarTables():
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE TB_USUARIOS (id serial PRIMARY KEY, nome varchar, email varchar, usernm varchar, data_nascimento date, senha varchar, CONSTRAINT unique_usernm UNIQUE(usernm))")
        cur.execute("CREATE TABLE TB_LIVROS(id serial PRIMARY KEY, titulo varchar, autor varchar, ano integer, editora varchar, alugado boolean not null)")
        cur.execute("CREATE TABLE TB_EMPRESTIMO(id serial PRIMARY KEY, nome varchar, CPF varchar, id_livro serial, FOREIGN KEY(id_livro) REFERENCES TB_LIVROS(id))")  
        con.commit()
        print("tabelas criadas!")
    except Exception as erro:
        print(erro)


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
    try:
        CriarTables()
        GravarLivros()
        cur = con.cursor()    
        con.commit()
        con.close()
    except Exception as erro:
        print(erro)    
except Exception as erro:
    print(erro)

    
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
    nome = str(input("digite o seu nome: "))
    email = str(input("digite o seu email: "))
    user = str(input("digite seu usuário: "))
    dtnsc = input("digite sua data de nascimento (dd-mm-aaaa): ")
    senha = mask.askpass(prompt="defina sua senha: ", mask="*")
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        print("conexão realizada")
    except Exception as erro:
        print(erro)
        
    cur = con.cursor()
    scpt = 'INSERT INTO TB_USUARIOS (nome, email, usernm, data_nascimento, senha) values (%s,%s,%s,%s,%s)'
    try:
        cur.execute(cur.mogrify(scpt,(f'{nome}',f'{email}',f'{user}',f'{dtnsc}',f'{senha}')))
        con.commit()
        con.close()
        print("Cadastro realizado com sucesso!")
        Main()
    except Exception as erro:
        print(erro)
    

def Login():
    user = str(input("digite seu usuário: "))
    senha = mask.askpass(prompt="digite sua senha: ", mask="*")

    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
        print("conexão realizada")
    except Exception as erro:
        print(erro)

    snh_scrpt = "SELECT senha FROM tb_usuarios WHERE usernm = %s"
    cur = con.cursor()
    cur.execute(snh_scrpt,(user,))
    result = cur.fetchone()
    if result == None:
        print("\nUsuário não cadastrado.\n")
        Main()
    else:
        for i in result:
            if i == senha:
                print("\nLogin feito com sucesso!\n")
                print("\nSeja-bem vindo(a)\n")
                Menu()
            else:
                print("Senha errada. Tente novamente.\n")
                Login()
    con.close()


def AlugarLivro():
    nmlivro = str(input("Digite o nome do livro: "))
    nmautor = str(input("Digite o nome do autor: "))
    script = "SELECT titulo, autor FROM tb_livros WHERE titulo = %s AND autor = %s"
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    cur.execute(script,(nmlivro,nmautor,))
    result = cur.fetchmany()
    if result == None:
        print("Livro não encontrado.")
        Menu()
    else:
        print(result)
    #SELECT
    #UPDATE


def DevolverLivro():
    r = 2
    #UPDATE


def ConsultarLivro():
    r = 2
    #SELECT


def CadastrarLivro():
    r = 2 
    #INSERT INTO TB_LIVROS


def RelatorioLivros():
    r = 2
    #SELECT * FROM TB_LIVROS or TB_EMPRESTIMOS & result.json()


def Menu():
    print("=-=-=-=-=-=-=-=-=-MENU=-=-=-=-=-=-=-=-=-")
    print('''
            1 - Alugar livro\n
            2 - Devolver livro\n
            3 - Consultar títulos\n
            4 - Cadastrar livro\n
            5 - Relatório\n
            6 - Sair
             ''')
    Mop = int(input('digite sua opção: '))

    if Mop == 1:
        AlugarLivro()
    elif Mop == 2:
        DevolverLivro()
    elif Mop == 3:
        ConsultarLivro()
    elif Mop == 4:
        CadastrarLivro()
    elif Mop == 5:
        RelatorioLivros()
    elif Mop == 6:
        Main()

Main()