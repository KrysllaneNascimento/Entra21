import sqlite3
import requests
from pycpfcnpj import cpfcnpj


class Cliente:
    def __init__(self, nome, cpf, cep):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep

    def cadastrar_novo(self, nomee, cpff, cepp):
        valida_cep = requests.get(f'https://viacep.com.br/ws/{cepp}/json/')
        if valida_cep.status_code == 200 and cpfcnpj.validate(cpff) == True:
            valida_cep = requests.get(f'https://viacep.com.br/ws/{cepp}/json/')
            rua = valida_cep.json()['logradouro']
            estado = valida_cep.json()['uf']
            cidade = valida_cep.json()['localidade']
            cursor.execute('INSERT INTO clientes (nome, cpf_cliente, cep_cliente ,'
                           'cidade_cliente, estado_cliente, rua_cliente)'
                           'VALUES (?, ?, ?, ?, ?, ?)', (nomee, cpff, cepp, cidade, estado, rua))
            cursor.execute('SELECT * FROM clientes')
            for cliente in cursor.fetchall():
                print(
                    f'{cliente[0]} - {cliente[1]} - {cliente[2]}- {cliente[3]} - {cliente[4]} - {cliente[5]}- {cliente[6]}')
        else:
            if valida_cep.status_code > 200:
                print('CLIENTE NÃO CADASTRADO DEVIDO AO CEP INVÁLIDO\nTente Novamente!')
            if cpfcnpj.validate(cpff) == False:
                print('CLIENTE NÃO CADASTRADO DEVIDO AO CPF INVÁLIDO\nTente Novamente!')
            if valida_cep.status_code > 200 and cpfcnpj.validate(cpff) == False:
                print('CEP E  CPF INVÁLIDO\nTente Novamente!')





class Produto:
    pass


class Vendas:
    pass


conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

c = Cliente('lorena', '11483190420', '89012160')
c.cadastrar_novo('Gabriel', '01966246498', '89021010')
