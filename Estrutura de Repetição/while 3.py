contador = 2
numero = 1
while numero <= 100:
    while contador < numero:
        if numero % contador == 0:
            break
        contador = contador + 1
    if contador == numero or numero == 2:
        print(numero)
    contador = 2
    numero = numero + 1