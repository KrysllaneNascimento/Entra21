def cont_letra(letra, palavra):
    cont = 0
    for i in palavra:
        if letra == i:
            cont += 1
    return cont


print(cont_letra('a', 'arara'))
