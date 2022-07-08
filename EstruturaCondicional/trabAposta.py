import random

escolhas = "1", "2"
carteira = 0
rodada = 0
lista = [0, 1]
print(50 * "-")
print("🤠 CASSINO 🤠".center(50))
print(50 * "-")
while True:
    rodada +=1
    sorteio = random.choice(escolhas)
    aposta = input("Digite quanto voce quer apostar: ")
    if aposta.isnumeric():
        escolha = input("Escolha (1)Cara ou (2)Coroa: ")
        print()
        if escolha == "1" or escolha == "2":
            if escolha == "1":
                escolhax = "Cara"
            else:
                escolhax = "Coroa"
            if sorteio == "1":
                sorteiox = "Cara"
            else:
                sorteiox = "Coroa"

            if escolha == sorteio:
                carteira += int(aposta)
                print("\033[0;32mVOCE GANHOU NESSA RODADA *-*\033[0;0m")
                if len(lista) > 3:
                    lista.pop(-2)
                    lista.pop()
                else:
                    lista = [0, 1]
            else:
                carteira -= int(aposta)
                print("\033[1;31mVOCE PERDEU NESSA RODADA -.-\033[0;0m ")
                lista.append(aposta)

            print(f'VOCÊ APOSTOU: {aposta},00\nVOCE ESCOLHEU: {escolhax}\nO RESULTADO FOI: {sorteiox}\nSEU SALDO FINAL É: {carteira},00\nESSA É A RODADA: {rodada}')
            print()
            n1 = lista[-2]
            n2 = lista[-1]
            n3 = int(n2) + int(n1)
            print(f"FIBONACCI RECOMENDA APOSTAR: {n3} R$")
            print()

        else:
            print("VALOR PARA APOSTA INVÁLIDO,REVISE OS ITENS DIGITADOS")
            print("")
    else:
        print("ESCOLHA INCORRETA,REVISE OS ITENS DIGITADOS")





















# ---------------------------------------------------------------------------------------------------------------------------------
# fibonacci jogador


import random

escolhas = "1", "2"
carteira = 0
rodada = 0
lista = [0, 1]
print(50 * "-")
print("🤠 CASSINO 🤠".center(50))
print(50 * "-")
n3 = "1"
while True:
    rodada +=1
    sorteio = random.choice(escolhas)
    aposta = str(n3)
    if aposta.isnumeric():
        escolha = random.choice(escolhas)
        print()
        if escolha == "1" or escolha == "2":
            if escolha == "1":
                escolhax = "Cara"
            else:
                escolhax = "Coroa"
            if sorteio == "1":
                sorteiox = "Cara"
            else:
                sorteiox = "Coroa"

            if escolha == sorteio:
                carteira += int(aposta)
                print("\033[0;32mVOCE GANHOU NESSA RODADA *-*\033[0;0m")
                if len(lista) > 3:
                    lista.pop(-2)
                    lista.pop()
                else:
                    lista = [0, 1]
            else:
                carteira -= int(aposta)
                print("\033[1;31mVOCE PERDEU NESSA RODADA -.-\033[0;0m ")
                lista.append(aposta)

            print(f'VOCÊ APOSTOU: {aposta},00\nVOCE ESCOLHEU: {escolhax}\nO RESULTADO FOI: {sorteiox}\nSEU SALDO FINAL É: {carteira},00\nESSA É A RODADA: {rodada}')
            print()
            n1 = lista[-2]
            n2 = lista[-1]
            n3 = int(n2) + int(n1)
            print(f"FIBONACCI RECOMENDA APOSTAR: {n3} R$")
            print()

        else:
            print("VALOR PARA APOSTA INVÁLIDO,REVISE OS ITENS DIGITADOS")
            print("")
    else:
        print("ESCOLHA INCORRETA,REVISE OS ITENS DIGITADOS")
    input()