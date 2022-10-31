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