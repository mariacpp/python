import psycopg2 as pg
import maskpass as mask
import json


def GravarLivros():
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        print("conexão realizada")
        try:
            cur = con.cursor()    
            script = """INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('a guerra dos tronos', 'george r.r. martin', 2019, 'suma', 'no');
            INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('a furia dos reis', 'george r.r. martin', 2019, 'suma', 'yes');
            INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES ('a tormenta das espadas', 'george r.r. martin', 2019, 'suma', 'no');"""
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
        cur.execute("CREATE TABLE TB_EMPRESTIMO(id serial PRIMARY KEY, nome varchar, CPF varchar, id_livro serial, FOREIGN KEY(id_livro) REFERENCES TB_LIVROS(id), CONSTRAINT unique_cpf UNIQUE(CPF))")  
        con.commit()
        print("tabelas criadas!")
    except Exception as erro:
        print(erro)


#CONECTAR NO BD
try:
    con = pg.connect(
        database="projeto",
        user="postgres",
        password="1234",
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
            password="1234",
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
            password="1234",
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
    print(type(nmlivro))
    print(nmlivro, nmautor)
    script = "SELECT id, titulo, autor FROM tb_livros WHERE titulo = %s AND autor = %s AND alugado = 'no';"
    'CREATE TABLE TB_EMPRESTIMO(id serial PRIMARY KEY, nome varchar, CPF varchar, id_livro serial, FOREIGN KEY(id_livro) REFERENCES TB_LIVROS(id))'
    
    
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    cur.execute(script,(nmlivro,nmautor,))
    resultado = cur.fetchone()
    if resultado == None:
        print("Livro não encontrado.")
        Menu()
    else:
        alugar = str(input('Deseja alugar? [s/n]: '))
        if alugar == 's':
            idlivro = resultado[0]
            print('DADOS DO LOCATÁRIO: ')
            nome = str(input('nome da pessoa: '))
            cpf = str(input('digite o cpf: '))
            scrptalg = 'INSERT INTO tb_emprestimo(nome,cpf,id_livro) values (%s,%s,%s)'
            cur.execute(scrptalg,(nome,cpf,idlivro,))
            alugado = "update tb_livros set alugado = 'yes' where id = %s;"
            cur.execute(alugado,(idlivro,))
            print("livro alugado com sucesso!")
            con.commit()
            con.close()
            Menu()
        else: 
            print('operação cancelada.')
            AlugarLivro()

def DevolverLivro():
    cpf = str(input('digite o cpf do locatário: '))
    script = "SELECT id_livro FROM tb_emprestimo WHERE cpf = %s;"
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    cur.execute(script,(cpf,))
    resultado = cur.fetchone()
    if resultado == None:
        print("Livro não encontrado.")
        Menu()
    else:
        devolver = str(input('Deseja devolver? [s/n]: '))
        if devolver == 's':
            idlivro = resultado[0]
            alugado = "update tb_livros set alugado = 'no' where id = %s;"
            cur.execute(alugado,(idlivro,))
            print("livro devolvido com sucesso!")
            con.commit()
            con.close()
            Menu()
        else: 
            print('operação cancelada.')
            DevolverLivro()

def ConsultarLivro():
    nm = str(input('informe o titulo do livro: '))
    scrpt = 'SELECT * FROM tb_livros WHERE titulo = %s'
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    cur.execute(scrpt,(nm,))
    resultado = cur.fetchall()
    print(resultado)
    con.close()
    for i in resultado:
        print(f'Titulo: {i[1]}\nAutor: {i[2]}\nAno: {i[3]}\nEditora: {i[4]}\nAlugado: {i[5]}\n')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
    Menu()

def CadastrarLivro():
    nm = str(input("digite o titulo do livro: "))
    aut = str(input("digite o autor da obra: "))
    ano = int(input('digite o ano de lançamento: '))
    editora = str(input('informe a editora: '))
    alugado = 'no'

    scrpt = 'INSERT INTO tb_livros(titulo, autor, ano, editora, alugado) VALUES (%s, %s, %s, %s, %s);'
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    try:
        cur.execute(scrpt,(nm,aut,ano,editora,alugado,))
        con.commit()
        print('livro cadastrado com sucesso!')
        con.close()
        Menu()
    except Exception as erro:
        print(erro)
        CadastrarLivro()

def RelatorioLivros():
    try:
        con = pg.connect(
            database="projeto",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
    except Exception as erro:
        print(erro)
    cur = con.cursor()
    script = 'SELECT * FROM tb_livros;'
    script2 = 'SELECT * FROM tb_emprestimo'
    cur.execute(script)
    resultado = cur.fetchall()
    cur.execute(script2)
    resultado2 = cur.fetchall()
    print(resultado)
    with open('relatório_livros.json','w') as write_file:
        json.dump(resultado, write_file)
        print('relatório gerado!')
    with open('relatório_livros.json','w') as write_file2:
        json.dump(resultado2, write_file2)
        print('relatório gerado!')
    con.commit()
    con.close()
    Menu()


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