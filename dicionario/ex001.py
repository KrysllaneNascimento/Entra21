# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre conforme abaixo: A situação deve ser gerada a partir de uma função def
#
# Aluno - Jonas Reiter
# Nota - 7.5
# Situação - APROVADO


def dicionario(input1, input2):
    chave = [input1]
    valor = input2
    novo_dic = dict.fromkeys(chave, valor)
    print(novo_dic)


nome = input('Digite seu nome: ')
nota = int(input('Digite sua nota: '))

dicionario(nome, nota)



