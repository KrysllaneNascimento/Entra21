# EX001:
# list = []
# s = 0
# cont = 0
#
# p = input('Deseja continuar?')
# while p == 's':
#     num = input('Digite um número:')
#     p = input('Deseja continuar?')
#     if p == 'n':
#         break
#     list.append(num)
#     s += int(list[cont])
#     cont += 1
#
# print('='*50)
# list.sort()
# print(f'NÚMEROS EM ORDEM CRESCENTE: {list}')
# list.sort(reverse=True)
# print(f'NÚMEROS EM ORDEM DECRESCENTE: {list}')
# print(s)
# print(f'média {s/(cont)}')

# EX002:

# total = 0
# list = []
# while True:
#     nome = input('Digite seu nome:')
#     list.append(nome)
#     total += 1
#     if nome == 'n':
#         break
# print('='*50)
# list.remove('n')
# list.sort()
# print(f'NOMES EM ORDEM CRESCENTE: {list}')
# list.sort(reverse=True)
# print(f'NOMES EM ORDEM DECRESCENTE: {list}')
# print(f'Total de nomes cadastrados: {total-1}')
# carlos = list.count('carlos')
# print(f'Foram cadastrados {carlos} nomes CARLOS na lista')

# EX003:

# Crie um algoritmo que receba valores aleatórios (de qualquer tipo), e ao final:
# A lista em ordem inversa ao que foi lançado
# quantos dados são de cada tipo: int, str, float, bool

# try:
#  print(a)
# except:
#   print(erro)

# list = []
# read = 0
# sub = 0
# while True:
#     for i in range(0, 6):
#         num = input('Digite algo:')
#         list.append(num)
#         tipo = list[i]
#         if tipo.isnumeric() == True:
#             read += 1
#             print('r', read)
#         else:
#             sub += 1
#             print('s', sub)



# list.remove(0)
# list.sort(reverse=True)
# print(list)


lista = []
i = 0
s = 0
f = 0
b = 0
while True:
    pergunta = input('Digite algo:')
    lista.append(pergunta)
    if pergunta == '.':
        break
    try:
        tipo = int(pergunta)
    except ValueError:
        try:
            tipo = float(pergunta)
        except ValueError:
            try:
                tipo = eval(pergunta)
            except NameError:
                s += 1
            else:
                b += 1
        else:
            f += 1
    else:
        i += 1
lista.pop()
lista.reverse()
print('-'*50)
print(f'Lista: {lista}')
print('-'*50)
print('Quantidade de Funcionalidades Digitadas:')
print(f'{s} String\n{i} Números Inteiros\n{f} Números Reais\n{b} Booleano')