# Criar um algoritmo quantos números você desejar (laço infinito), e ao final dele mostre:
# A lista em ordem crescente
# A lista em ordem decrescente
# A soma de todos os itens
# A média de todos os números
#
#
#
# Crie um algoritmo que receba quantos nomes(apenas nome) desejar, e ao final:
# A lista em ordem crescente
# A lista em ordem decrescente
# O total de nomes cadastrados
# Quantos ‘Carlos’ existem na lista
#
# Crie um algoritmo que receba valores aleatórios (de qualquer tipo), e ao final:
# A lista em ordem inversa ao que foi lançado
# quantos dados são de cada tipo: int, str, float, bool

list = []

while True:
    num = int(input('Digite um número:'))
    list.append(num)
    if num == 0:
        break
