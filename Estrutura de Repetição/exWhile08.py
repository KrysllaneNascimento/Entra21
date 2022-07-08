# 8.  	Crie um programa que receba um número indeterminado de anos. Ao final, apresente quantos anos são pares,
# quantos são ímpares, quantos são bissextos, quantos são futuros (2023, 2024), e quantos são passado (2000, 2010)
ano_par = 0
ano_impar = 0
ano_bis = 0
futuro = 0
passado = 0
while True:
    ano = int(input('Digite um ano: '))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        ano_bis += 1

    if ano > 2022 and ano != 0:
        futuro += 1
    elif ano < 2022 and ano != 0:
        passado += 1

    if ano % 2 == 0 and ano != 0:
        ano_par += 1
    else:
        ano_impar += 1

    if ano == 0:
        break

print('PARES: ', ano_par)
print('ÍMPARES: ', ano_impar)
print('BISSEXTOS: ', ano_bis)
print('FUTUROS: ', futuro)
print('PASSADOS: ', passado)
# 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052