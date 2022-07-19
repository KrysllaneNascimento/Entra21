import sqlite3


def CriaPOkemon(nome, tipo, pokedex, level):
    cursor.execute('INSERT INTO lista_pokemons(nome, tipo, pokedex, level)'
                   'VALUES (?, ?, ?, ?)', (nome, tipo, pokedex, level))
    conexao.commit()


def EvoluirPokemon():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'Id:{pokemon[0]}\nNome:{pokemon[1]}\nTipo:{pokemon[2]}\nPoxedex:{pokemon[3]}\nLevel:{pokemon[4]}')
        print('=' * 20)
    tipo = int(input('Digite o id do pokemon que você deseja mudar o nível: '))
    nivel = int(input('Digite o valor do novo nível: '))
    cursor.execute(f'UPDATE lista_pokemons SET level={nivel} WHERE id={tipo}')
    conexao.commit()


def EditarPokemon():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'Id:{pokemon[0]}\nNome:{pokemon[1]}\nTipo:{pokemon[2]}\nPoxedex:{pokemon[3]}\nLevel:{pokemon[4]}')
        print('=' * 20)
    poke = int(input('Digite o id do pokemon que deseja mudar: '))
    mudar = input('Deseja muda:\n[1]NOME [2]TIPO [3]POKEDEX [4] LEVEL')
    if mudar == '1':
        nome = input('Digite o novo nome: ')
        cursor.execute(f'UPDATE lista_pokemons SET nome={nome} WHERE id={poke}')
        conexao.commit()
    elif mudar == '2':
        tipo = input('Digite o novo Tipo: ')
        cursor.execute(f'UPDATE lista_pokemons SET tipo={tipo} WHERE id={poke}')
        conexao.commit()
    elif mudar == '3':
        tipo = input('POKEDEX: ')
        cursor.execute(f'UPDATE lista_pokemons SET tipo={tipo} WHERE id={poke}')
        conexao.commit()
    elif mudar == '4':
        tipo = int(input('Novo level: '))
        cursor.execute(f'UPDATE lista_pokemons SET tipo={tipo} WHERE id={poke}')
        conexao.commit()


def ListarPokemon():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'Id:{pokemon[0]}\nNome:{pokemon[1]}\nTipo:{pokemon[2]}\nPoxedex:{pokemon[3]}\nLevel:{pokemon[4]}')
        print('=' * 20)


def Deletar():
    cursor.execute('SELECT * FROM lista_pokemons')
    for pokemon in cursor.fetchall():
        print(f'Id:{pokemon[0]}\nNome:{pokemon[1]}\nTipo:{pokemon[2]}\nPoxedex:{pokemon[3]}\nLevel:{pokemon[4]}')
        print('='*20)
    tipo = input('Digite o Id do pokemon que deseja deletar: ')
    cursor.execute(f'DELETE FROM lista_pokemons WHERE id={tipo}')
    conexao.commit()


conexao = sqlite3.connect('banco pokemon.db')
cursor = conexao.cursor()



ListarPokemon()


cursor.close()
conexao.close()