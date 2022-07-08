# Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão
# nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while True:
    num = int(input('DIGITE UM NÚMERO: '))
    if num < 0:
        break
    else:
        if num <= 25:
            cont1 += 1
        elif num > 25 and num <= 50:
            cont2 += 1
        elif num > 50 and num <= 75:
            cont3 += 1
        elif num > 75 and num <= 100:
            cont4 += 1

print(f'Números digitados de [0-25]{cont1}')
print(f'Número digitados de [26-50]{cont2}')
print(f'Número digitados de [51-75] {cont3}')

# if num <= 25:
#     cont1 += 1
# elif num > 25 <= 50:
#     cont2 += 1
# elif 50 < num <= 75:
#     cont3 += 1
# elif 75 < num <= 100:
#     cont4 += 1



