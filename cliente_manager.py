import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.sqlite')

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row  

def criar_tabela(conexao, cursor):
    cursor.execute(
        " CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150)) "
    )
    conexao.commit()

def inserir_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(f" INSERT INTO clientes (nome, email) VALUES (?, ?); ", data)
    conexao.commit()

def update_cliente(conexao, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute(f" UPDATE clientes SET nome = ?, email = ? WHERE id = ?; ", data)
    conexao.commit()    

def remover_cliente(conexao, cursor, id):
    data = (id,)
    cursor.execute(f" DELETE FROM clientes WHERE id = ?; ", data)
    conexao.commit()

def inserir_varios_clientes(conexao, cursor, dados):
    cursor.executemany(" INSERT INTO clientes (nome, email) VALUES (?, ?); ", dados)
    conexao.commit()

def consultar_clientes(cursor):
    cursor.execute(" SELECT id, nome, email FROM clientes; ")
    for linha in cursor.fetchall():
        print(linha)

def consultar_cliente_por_id(cursor, id):
    data = (id,)
    cursor.execute(" SELECT id, nome, email FROM clientes WHERE id = ?; ", data)
    print(cursor.fetchone())    

def consultar_cliente_por_nome(cursor, nome):
    data = (f"%{nome}%",)
    cursor.execute(" SELECT id, nome, email FROM clientes WHERE nome LIKE ?; ", data)
    for linha in cursor.fetchall():
        print(linha)

def consultar_clientes_por_email(cursor, email):
    data = (f"%{email}%",)
    cursor.execute(" SELECT id, nome, email FROM clientes WHERE email LIKE ?; ", data)
    for linha in cursor.fetchall():
        print(linha)

def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row            
    cursor.execute(" SELECT id, nome, email FROM clientes WHERE id = ?; ", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

# MENUS DE TESTE
# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(cliente)
# cliente = recuperar_cliente(cursor, 5)
# print(dict(cliente))
# print(cliente['nome'], cliente['email'])
# print(f'{cliente["nome"]}, SEJA BEM VINDO(A) AO SISTEMA ')

#FORMA VULNERÁVEL
# id_cliente = input("Digite o ID do cliente que deseja consultar: ")
# cursor.execute("SELECT * FROM clientes WHERE id={id_cliente}") # <- Vulnerável a SQL Injection
# cliente = cursor.fetchall()
# for cliente in cliente:
#     print(dict(cliente))

#FORMA SEGURA
# id_cliente = input("Digite o ID do cliente que deseja consultar: ")
# cursor.execute("SELECT * FROM clientes WHERE id=?;", (id_cliente,))
# cliente = cursor.fetchall()
# for cliente in cliente:
#     print(dict(cliente))


#TRATAMENTO DE ERRO 
try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", ("TESTE3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?);", (4, "TESTE4", "teste4@gmail.com"))
    conexao.commit()
except Exception as e:
    print("Erro ao inserir dados: ", e)
    conexao.rollback()
