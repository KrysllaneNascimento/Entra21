from random import randint
from time import sleep




def transformarInputJokenpo(input, nomeJogado):
    if input == 1:
        print(f'{nomeJogado} jogou PEDRA')
    elif input == 2:
        print(f'{nomeJogado} jogou PAPEL')
    elif input == 3:
        print(f'{nomeJogado} jogou TESOURA')
    else:
        print(f'O {nomeJogado} fez uma jogada inválida')


def jogadaMaquina():
    valor = randint(1, 3)
    return valor


def apresentacaoJogada():
    sleep(0.5)
    print('\033[31mJO\033[m'.center(20))
    sleep(1)
    print('\033[32mKEN\033[m'.center(30))
    sleep(1)
    print('\033[33mPO\033[m'.center(40))
    print('°'*40)
    sleep(0.5)


def menu():
    linha = '*' * 40
    print(linha)
    print('\033[32mOPÇÕES:\033[m'.center(45))
    print('''[ 1 ] PEDRA
             [ 2 ] PAPEL
             [ 3 ] TESOURA'''.center(90))
    print(linha)


def definirGanhador(jogada1, jogada2):
    if jogada1 == jogada2:
        return 0
    if jogada1 == 1 and jogada2 == 2:
        print('\033[34mPapel ENVOLVE Pedra\033[m')
        return jogada2
    if jogada1 == 1 and jogada2 == 3:
        print('\033[31mPedra QUEBRA Tesoura\033[m')
        return jogada1
    if jogada1 == 2 and jogada2 == 3:
        print('\033[35mTesoura CORTA Papel\033[m')
        return jogada2
    if jogada2 == 1 and jogada1 == 2:
        print('\033[34mPapel ENVOLVE Pedra\033[m')
        return jogada1
    if jogada2 == 1 and jogada1 == 3:
        print('\033[31mPedra QUEBRA Tesoura\033[m')
        return jogada2
    if jogada2 == 2 and jogada1 == 3:
        print('\033[35mTesoura CORTA Papel\033[m')
        return jogada1
    return -1
