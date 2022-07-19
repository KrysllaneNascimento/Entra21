import requests
from pycpfcnpj import cpfcnpj
ender = input('Digite seu cep: ')
cpff = input('Digite: ')
valida_cep = requests.get(f'https://viacep.com.br/ws/{ender}/json/')
if valida_cep.status_code > 200:
    print('CLIENTE NÃO CADASTRADO DEVIDO AO CEP INVÁLIDO\nTente Novamente!')
if cpfcnpj.validate(cpff) == False:
    print('CLIENTE NÃO CADASTRADO DEVIDO AO CPF INVÁLIDO\nTente Novamente!')
if valida_cep.status_code > 200 and cpfcnpj.validate(cpff) == False:
    print('CEP E  CPF INVÁLIDO\nTente Novamente!')

# rua = cep.json()['logradouro']
# estado = cep.json()['uf']
# cidade = cep.json()['localidade']

