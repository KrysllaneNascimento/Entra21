#BANCO DE DADOS
# RELACIONAL:
#SQL - MySQL, Postgreem, SQLite, OracleDataBase, FireBase,FireBird
# NÃO RELACIONAL :
#NOSQL , Not Only SQL
#Dimensão : Tabela onde os fatos estão acontecendo
#Fato : Tabel onde compõe os fatos que podem ocorrer
#STAR SCHEMA - Tabela mais importante no centro e as outras ao lado
#CRUD - Create, Read, Update ,Delete
#Criar - create- comando inserte
# Read - ler as informações já cadastradas -comando select
#update - para atualizar - comando update
#delete - apagar uma tabela, banco de dados, etc. - comando Delete ou drop.

import sqlite3

conexao = sqlite3.connect('Meu primeiro banco.db')
cursor = conexao.cursor()

# Criar tabela - C
cursor.execute('CREATE TABLE IF NOT EXISTS frutas('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome_fruta TEXT,'
               'variedade TEXT)')
conexao.commit()

# Inserir dados na tabela- C

# cursor.execute('INSERT INTO frutas(nome_fruta, variedade)'
#                'VALUES ("Banana","Amarela")')
# conexao.commit()


# #Atualizar regristo - U
# cursor.execute('UPDATE frutas SET variedade="Branca" WHERE id=3')
# conexao.commit()

# Deletar - D - FROM apaga os registros da tabela e NÃO A TABELA

# cursor.execute('DELETE FROM frutas WHERE id=3')
# conexao.commit()

#Buscar dados - R
# cursor.execute('SELECT * FROM frutas')
# for fruta in cursor.fetchall():
#     print(f'{fruta[0]} - {fruta[1]} - {fruta[2]}')

#Deletar tabela - D
# cursor.execute('DROP TABLE frutas')
# conexao.commit()

cursor.close()
conexao.close()


