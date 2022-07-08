from corpo05 import apresentacaoJogada
from corpo05 import definirGanhador
from corpo05 import jogadaMaquina
from corpo05 import transformarInputJokenpo
from corpo05 import menu

jogouPedra = False
podeJogar = True
pontosJogador = 0

pontosMaquina = 0
totPedra = 0
# menu()

for i in range(5):
    menu()
    podeJogar = True
    while podeJogar:
        jogador = int(input('Digite sua Escolha:'))
        if jogador == 1 and jogouPedra == True:
            podeJogar = True
            print('Pedra Jogada 2x JOGADA INVÁLIDA')
        elif jogador == 1:
            jogouPedra = True
            podeJogar = False
        else:
            jogouPedra = False
            podeJogar = False

    apresentacaoJogada()
    transformarInputJokenpo(jogador, 'Jogador')
    jogadaMaq = jogadaMaquina()
    transformarInputJokenpo(jogadaMaq, 'Computador')
    ganhador = definirGanhador(jogador, jogadaMaq)
    if ganhador == 0:
        print('EMPATE')
    elif ganhador == jogador:
        print('Jogador venceu')
        pontosJogador += 1
    elif ganhador == jogadaMaq:
        print('Computador venceu')
        pontosMaquina += 1
    else:
        print('Partida inválida')

print('*' * 40)
if pontosJogador > pontosMaquina:
    print(f'Jogador venceu {pontosJogador}x e Computador venceu {pontosMaquina}x')
    print(f'Jogador foi o Campeão')
elif pontosMaquina > pontosJogador:
    print(f'Jogador venceu {pontosJogador}x e Computador venceu {pontosMaquina}x')
    print('Computador foi o Campeão')
else:
    print(f'Jogador ganhou {pontosJogador}x e Computador ganhou {pontosMaquina}x')
    print(f'Houve um EMPATE')

