# from random import randint
#
# arquivo = open('listatimes.txt','r')
# times = arquivo.read().splitlines()
# continuar = "S"
#
#
# while True:
#     pontos = [0] * len(times)
#     cont_casa = 0
#     cont_visita = 0
#     for i in times:
#         for j in times:
#             if i == j:
#                 cont_visita += 1
#                 continue
#             placar_casa = randint(0, 6)
#             placar_visita = randint(0, 6)
#             print(f'{i} [{placar_casa}] x [{placar_visita}] {j}')
#             if placar_casa > placar_visita:
#                 pontos[cont_casa] += 3
#             elif placar_visita > placar_casa:
#                 pontos[cont_visita] += 3
#             else:
#                 pontos[cont_casa] += 1
#                 pontos[cont_visita] += 1
#
#             cont_visita += 1
#         cont_visita = 0
#         cont_casa += 1
#
#     print(pontos)
#     maior_pont = max(pontos)
#     time_campeao = pontos.index(maior_pont)
#
#     print(f"CAMPEAO 2022 {times[time_campeao]} com {maior_pont} pontos")
#     ranking = []
#     for i in range(len(times)):
#         ranking.append(f'{pontos[i]} - {times[i]}')
#
#     ranking.sort(reverse=True)
#
#     print()
#     for i in ranking:
#         print(i)
#
#     opcao = input('Deseja continuar? ').upper()
#
#     if opcao == "S":
#         continue
#     else:
#         break



num = int(input('Digite um número: '))
print('Escolha uma das bases para conversão:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
op = int(input('Sua opção: '))

if op == 1:
    op1 = "{0:b}".format(num)
    print(op1)