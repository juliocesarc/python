import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='#7if@%md&9!w17#',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        print('conexão fechada')
        conexao.close()
"""   
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('Julio', 'César', 17, 61.5))
        conexao.commit()
"""
"""
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        dados = [
            ('Luana', 'Pereira', 38, 70),
            ('Edson', 'Santos', 54, 78),
            ('Giovanna', 'Costa', 10, 40)
        ]
        cursor.executemany(sql, dados)
        conexao.commit()
"""

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente['nome'], cliente['id'])

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id=%s'
        cursor.execute(sql, (2,))
        conexao.commit()