import sqlite3
import os


pasta_atual = os.path.dirname(__file__)
conexao = sqlite3.connect(f'{pasta_atual}/basededados.db')
cursor = conexao.cursor()

""" Cria uma tabela clientes caso a mesma ainda não exista
nela temos uma coluna 'id' que é um número inteiro, auto 
incrementado pela própria base de dados.
temos uma coluna nome, cuja mesma recebe um texto, e uma 
coluna peso que possui seus valores reais ou seja, de ponto 
flutuante de simples precisão"""
#cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#'nome TEXT,'
#'peso REAL'
#')')

""" Insere valores de nome e peso na tabela clientes """
#cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Luana Pereira', 38))
#conexao.commit()

""" Altera o nome do id 2 que antes era Julio, para Maria """
#cursor.execute('UPDATE clientes SET nome=? WHERE id=?', ('Maria', 2))
#conexao.commit()

""" Deletou o índice 4, estava repetido, 4 Luana Pereira 38.0 """
#cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 4})
#conexao.commit()

""" Selecionou o id, nome e peso (poreria umas um * no lugar)
somente onde o peso era maior que 50 """
cursor.execute('SELECT id, nome, peso FROM clientes WHERE peso > :peso', {'peso': 50.0})

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)



cursor.close()
conexao.close()