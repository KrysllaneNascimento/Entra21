# Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.


contador = 100
while contador <= 200:
    if contador % 2 != 0:
        print(contador)
    contador += 1
