def conta_numeros(num):
    cont = 0
    for i in str(num):
        cont += 1
    return cont


print(conta_numeros(1000))