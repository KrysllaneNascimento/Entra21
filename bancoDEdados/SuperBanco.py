import sqlite3
import requests
from pycpfcnpj import cpfcnpj

conexao = sqlite3.connect('vendasserrs.db')
cursor = conexao.cursor()


def conex():
    return conexao.commit()


def execute(*args):
    return cursor.execute(*args)


class Cliente:
    def __init__(self):
        pass

    def insert(self):
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu cpf ').replace('.', '').replace('-', '')
        cep = input('Digite seu cep: ').replace('-', '')
        valida_cep = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        a = cpfcnpj.validate(cpf)
        if valida_cep.status_code == 200 and a:
            rua = valida_cep.json()['logradouro']
            estado = valida_cep.json()['uf']
            cidade = valida_cep.json()['localidade']
            sql = f"INSERT INTO clientes (nome_cliente, cpf_cliente, cep_cliente ,cidade_cliente, estado_cliente, rua_cliente) VALUES {nome, cpf, cep, cidade, estado, rua}"
            execute(sql)
            conex()
            print('Novo cadastro criado')
        else:
            if not a and valida_cep.status_code != 200:
                print('CEP  e CPF INVÁLIDO')
            elif valida_cep.status_code != 200:
                print('CEP INVÁLIDO')
            elif not a:
                print('CPF INVÁLIDO')

    def update(self):
        dic = {'1': 'nome_cliente', '2': 'cpf_cliente', '3': 'cep_cliente'}
        cpf = input('Digite seu cpf: ').replace('.', '').replace('-', '')
        tipo_registro = input(f'1.Nome  |  2.CPF   |  3.Cep  |\nDigite oque deseja atualizar: ')
        novo_dado = input('Informe o novo registro: ').replace('-', '').replace('.', '')
        lista = []
        cursor.execute(f" SELECT cpf_cliente FROM clientes WHERE cpf_cliente='{cpf}' ")
        for cliente in cursor.fetchall():
            lista.append(cliente)
        if len(lista) > 0:
            sql = f"UPDATE clientes SET '{dic[tipo_registro]}' = '{novo_dado}' WHERE cpf_cliente='" + cpf + "'"
            execute(sql)
            conex()
            print('Cadastro atualizado!')
        else:
            print('Dados inválidos!')

    def delete(self):
        cpf = input('Digite seu CPF: ').replace('-', '').replace('.', '')
        cursor.execute(f'SELECT CPF_cliente FROM vendas WHERE CPF_cliente="{cpf}"')
        lista = []
        for cliente in cursor.fetchall():
            lista.append(cliente)
        if lista is not None:
            sql_vendas = f"DELETE FROM vendas WHERE CPF_cliente='{cpf}'"
            execute(sql_vendas)
            conex()
            sql_clientes = f"Delete FROM clientes WHERE cpf_cliente='{cpf}'"
            execute(sql_clientes)
            conex()
            print('Cadastro Excluido com sucesso !')
        else:
            sql = f"Delete FROM clientes WHERE cpf_cliente='{cpf}'"
            execute(sql)
            print('Cadastro Excluido')
            conex()


class Produto:
    def __init__(self):
        pass

    def insert(self=0):
        cod_b = input('Código de barras: ')
        nome_prod = input('Nome do produto: ')
        fabricante_prod = input('Nome do fabricante')
        sql = f"INSERT INTO produtos (cod_barras, nome_produto,fabricante_produto) VALUES {cod_b, nome_prod, fabricante_prod}"
        execute(sql)
        conex()
        print('Produto inserido com sucesso!')

    def update(self):
        dic = {'1': 'Cod_barras', '2': 'nome_fabricante', '3': 'nome_produto'}
        cod_barras = input('Código de barras: ')
        tipo_registro = input(f'1.Código de barras\n2.Nome do fabricante\n3.Nome do produto\nDigite sua escolha: ')
        novo_registro = input('Informe o novo registro: ')
        lista = []
        cursor.execute(f" SELECT cod_barras FROM produtos WHERE cod_barras='{cod_barras}' ")
        for produto in cursor.fetchall():
            lista.append(produto)
        if len(lista) > 0:
            sql = f"UPDATE produtos SET '{dic[tipo_registro]}' = '{novo_registro}' WHERE cod_barras = {cod_barras}"
            execute(sql)
            conex()
        else:
            print('Código de barras inválido')

    def delete(self=0):
        cod_barras = input('Código de barras: ')
        lista = []
        cursor.execute(f" SELECT Cod_barras FROM vendas WHERE Cod_barras='{cod_barras}' ")
        for cliente in cursor.fetchall():
            lista.append(cliente)
        if lista is not None:
            sql_vendas = f"DELETE FROM vendas WHERE Cod_barras='{cod_barras}'"
            execute(sql_vendas)
            conex()
            sql_produto = f"Delete FROM produtos WHERE cod_barras='{cod_barras}'"
            execute(sql_produto)
            conex()
            print('Item Excluido com sucesso !')
        else:
            sql_produto = f"Delete FROM produtos WHERE cod_barras='{cod_barras}'"
            execute(sql_produto)
            conex()
            print('Item Excluido com sucesso !')


class Vendas:
    def __init__(self):
        pass

    def insert(self):
        data_venda = input('Data da venda: ')
        hora_venda = input('Hora da venda: ')
        cpf_cliente = input('CPF: ').replace('-', '').replace('.', '')
        cod_barras = input('Código de barras: ')
        quantidade = float(input('Quantidade do produto: '))
        valor_uni = float(input('Valor unitario: '))
        valor_tot = float(input('Valor total da venda: '))
        lista_prod = []
        lista_cliente = []
        cursor.execute(f" SELECT cod_barras FROM produtos WHERE cod_barras={cod_barras} ")
        for cliente in cursor.fetchall():
            lista_cliente.append(cliente)

        cursor.execute(f"SELECT cpf_cliente FROM clientes WHERE cpf_cliente={cpf_cliente}")
        for produto in cursor.fetchall():
            lista_prod.append(produto)

        if len(lista_cliente) < 1 and len(lista_prod) < 1:
            print('USUÁRIO NÃO CADASTRADO\nCadastre-se abaixo!')
            a = Cliente()
            a.insert()
            print('Cliente criado!')
            print('=' * 50)
            print('Código de barras não cadastrado\nCadastre-o abaixo!')
            b = Produto()
            b.insert()
            sql_venda = f"INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, Cod_barras, quantidade, valor_unitario, valor_total) VALUES {data_venda, hora_venda, cpf_cliente, cod_barras, float(quantidade), float(valor_uni), float(valor_tot)} "
            execute(sql_venda)
            conex()
            print('Venda registrada !')
        else:
            if len(lista_cliente) < 1 and len(lista_prod) > 0:
                print('USUÁRIO NÃO CADASTRADO\nCadastre-se abaixo!')
                a = Cliente()
                a.insert()
                print('Cliente criado!')
                sql_venda = f"INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, Cod_barras, quantidade, valor_unitario, valor_total) VALUES {data_venda, hora_venda, cpf_cliente, cod_barras, float(quantidade), float(valor_uni), float(valor_tot)} "
                print('Venda registrada !')
                execute(sql_venda)
                conex()
            elif len(lista_prod) < 1 and len(lista_cliente) > 0:
                print('Produto não cadastrado\nCadastre-o abaixo!')
                c = Produto()
                c.insert()
                sql_venda = f"INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, Cod_barras, quantidade, valor_unitario, valor_total) VALUES {data_venda, hora_venda, cpf_cliente, cod_barras, float(quantidade), float(valor_uni), float(valor_tot)} "
                execute(sql_venda)
                conex()
                print('Informações da venda criada !')

            else:
                sql_venda = f"INSERT INTO vendas (data_venda, hora_venda, CPF_cliente, Cod_barras, quantidade, valor_unitario, valor_total) VALUES {data_venda, hora_venda, cpf_cliente, cod_barras, float(quantidade), float(valor_uni), float(valor_tot)} "
                execute(sql_venda)
                conex()

    def update(self):
        cpf = input('Digite seu CPF: ')
        print('=' * 30)
        tipo_registro = input(
            f'1.Código de barras\n2.Hora da venda\n3.Data da venda\n4.Quantidade\n5.Valor unitario\n6.Valor total\n7.CPF\nDigite sua escolha: ')
        if 3 < int(tipo_registro) < 7:
            novo_registro = float(input('Digite os dados: '))
            print('=' * 30)
        else:
            novo_registro = input('Digite os dados: ')
            print('=' * 30)
        dic = {'1': 'Cod_barras', '2': 'hora_venda', '3': 'data_venda', '4': 'quantidade', '5': 'valor_unitario',
               '6': 'valor_total', '7': 'CPF_cliente'}
        lista = []
        cursor.execute(f" SELECT CPF_cliente FROM vendas WHERE CPF_cliente='{cpf}' ")
        for cliente in cursor.fetchall():
            lista.append(cliente)
        if len(lista) > 0:
            sql = f"UPDATE vendas SET '{dic[tipo_registro]}' = '{novo_registro}' WHERE cpf_cliente='" + cpf + "'"
            execute(sql)
            conex()
            print('Informações atualizadas')
        else:
            print('Cpf inválido')

    def delete(self):
        cod_barras = input('Digite o código de barras: ')
        lista = []
        cursor.execute(f" SELECT Cod_barras FROM vendas WHERE Cod_barras='{cod_barras}' ")
        for vendas in cursor.fetchall():
            lista.append(vendas)
        if len(lista) > 0:
            sql_vendas = f"DELETE FROM vendas WHERE Cod_barras='{cod_barras}'"
            execute(sql_vendas)
            conex()
            print('Item Excluido com sucesso !')
        else:
            print('Código de barras não está  cadastrado!')

    def ListarVenda_CPF(self):
        lista = []
        cpf = input('Digite seu cpf: ').replace('.', '').replace('-', '')
        cursor.execute(f"SELECT * FROM vendas WHERE CPF_cliente='{cpf}' ")
        for cliente in cursor.fetchall():
            lista.append(cliente)
            print(
                f"Id: {cliente[0]} - Data da venda: {cliente[1]} - Hora da venda: {cliente[2]} - CPF: {cliente[3]}-\n"
                f"Código de barras: {cliente[4]} Quantidade:{cliente[5]} - Valor Unitário: {cliente[6]} - Valor total: {cliente[7]}")
            print('=' * 100)
        if len(lista) == 0:
            print('*'*55)
            print(f'Não foram encontrados compras para o CPF {cpf}')
            print('*' * 55)

    def rankingvenda_produto(self):
        lista = []
        dic = {}
        total = a = 0
        cursor.execute(f"SELECT cod_barras FROM produtos")
        for cod in cursor.fetchall():
            lista.append(cod)
        for i in lista:
            cursor.execute(f'SELECT * FROM vendas WHERE Cod_barras= "{i}" ')
            for venda in cursor.fetchall():
                print(venda)


def todos():
    dic = {'1': Cliente.insert, '2': Cliente.update, '3': Cliente.delete, '4': Produto.insert, '5': Produto.update,
           '6': Produto.delete, '7': Vendas.insert, '8': Vendas.update, '9': Vendas.delete,
           '10': Vendas.ListarVenda_CPF, '11': Vendas.rankingvenda_produto}
    print(f'OPÇÕES:\n'
          '1.Cadastrar novo Cliente\n'
          '2.Atualizar cadastro do Cliente\n'
          '3.Deletar cadastro do Cliente\n'
          '4.Cadastrar novo Produto\n'
          '5.Atualizar cadastro do Produto\n'
          '6.Deletar cadastro do Produto\n'
          '7.Cadastrar nova Venda\n'
          '8.Atualizar registro da Venda\n'
          '9.Deletar registro da Venda\n'
          '10.Consultar todas as suas compras\n'
          '11.Ranking de vendas por produto')
    op = input('Digite sua escolha: ')
    return dic[op]('self')
