# Crie uma calculadora que receba:  Valor presente(valor a ser financiado),
# Taxa de Juros Mensal e Nº de meses que será parcelada a compra.
# A calculadora deverá perguntar qual tipo de amortização será utilizada, PRICE ou SAC,
# e retornar ao final a lista com os valores de cada período, conforme imagem de exemplo.
print('\033[1;33m='*30)
print('\033[1;34mCAMPEONATO BRASILEIRO'.center(30))
print()
time = ['Vasco', 'Flamengo', 'Palmeiras']
time2 = time

for i in time:
    for j in time2:
        if i == j:
            continue
        print(f'{i}[] x []{j}')



