# def cont(f):
#     les = f.count('a')
#     return les


# def rev(num):
#     return num[::-1]

# def quatro(num):
#     return len(num)

# def usuario(escolha):
#     if escolha == 1:
#         escolha = 'Pedra'
#     elif escolha == 2:
#         escolha = 'Papel'
#     elif escolha == 3:
#         escolha = 'Tesoura'

def maq(maquina):
     return f'Adversário: {maquina}'

def ganhador(escolha,maquina):
    if escolha == 1 and maquina == 1:
        print('Houve um EMPATE')
    elif escolha == 1 and maquina == 2:
        print('')
