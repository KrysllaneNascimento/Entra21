import sqlite3

conexao = sqlite3.connect('Banco de dados.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'cpf TEXT,'
               'nome TEXT,'
               'data_nascimento TEXT,'
               'cep TEX,'
               'peso REAL,'
               'altura REAL)')
conexao.commit()
cpf = input('Digite seu CPF: ')
nome = input('Digite seu nome: ')
data_nasc = input('Digite sua data de nascimento: ')
cep = input('Digite seu CEP: ')
peso = float(input('Digite seu Peso: '))
alt = float(input('Digite sua Altura: '))

cursor.execute('INSERT INTO clientes(cpf, nome, data_nascimento, cep, peso, altura)'
               'VALUES(?, ?, ?, ?, ?, ?)', (cpf, nome, data_nasc, cep, peso, alt))
conexao.commit()

cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(f'{cliente[0]} - {cliente[1]} - {cliente[2]} - {cliente[3]} - {cliente[4]} - {cliente[5]} - {cliente[6]}')

cursor.close()
conexao.close()