from random import randint
print('\033[1;33m~'*30)
print('\033[1;32mCAMPEONATO BRASILEIRO'.center(30))
print('\033[1;33m~'*30)
print('Quantos times vão participar do Campeonato? ')
quant = int(input('Resposta: '))
print()
time = []
time2 = time

for i in range(quant):
    novo_time = input(f'\033[0;34mDigite o {i+1} Time: ')
    time.append(novo_time)
    print()
print('-'*30)
print('RODADAS DO JOGO:')

for i in time:
    for j in time2:
        if i == j:
            continue
        valor1 = randint(0, 10)
        valor2 = randint(0, 10)
        print(f'\033[1;31m{i}[{valor1}] x [{valor2}]{j}')
        if valor1 == valor2:
            print('\033[0;30mEMPATE')
            print('\033[0;33m=' * 30)
        if valor1 > valor2:
            print(f'\033[0;32m{i} TIME VENCEDOR ')
            print('\033[0;33m=' * 30)
        if valor2 > valor1:
            print(f'\033[0;36m{j} TIME VENCEDOR')
            print('\033[0;33m=' * 30)