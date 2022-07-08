from datetime import date
maior = 0
menor = 0
data_atual = date.today().year

for i in range(1, 8):
    ano_nasc = int(input(f'Ano de nascimento {i}° Pessoa:'))
    print('-'*35)
    idade = data_atual - ano_nasc
    if idade < 21:
        menor += 1
    elif idade > 21:
        maior += 1
print(f'{menor} pessoas ainda NÃO atingiram a MAIOR IDADE')
print(f'{maior} pessoas JÁ atingiram a MAIOR IDADE  ')

