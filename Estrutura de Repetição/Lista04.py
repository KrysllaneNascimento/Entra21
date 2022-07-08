soma = 0
num_positivo = 0
num_negativo = 0
perc_positivo = 0
perc_negativo = 0
num_maximo = 0
num_minimo = 0
cont = 0

pergunta = input('\033[1;31mDeseja fazer cálculos aritméticos? [s] ou [n]: ')
if pergunta.isalpha() == False:
    print('\033[1;35;40mOpção inválida, insira [S] ou [N]\033[m')
else:
    while pergunta == 's':
        cont += 1
        num = int(input('\033[1;34mDigite um valor: '))
        soma += num
        pergunta = input('\033[1;32mDeseja adicionar mais valores[s] ou [n]: ')

        if num > 0:
            num_positivo += 1
        else:
            num_negativo += 1


        if num > num_maximo or cont == 1:
            num_maximo = num

        if num < num_minimo or cont == 1:
            num_minimo = num

    perc_positivo = (num_positivo * 100) / cont
    perc_negativo = (num_negativo * 100) / cont
    media = soma / cont

    print('-' * 50)
    print(f'\031[0;30mA média entre os número digitados é igual a {media:.2f}')
    print()
    print(f'\033[0;33mForam digitados {num_positivo:.2f} valor(es) POSITIVO')
    print(f'\033[0;32mPercentual de números Positivos: {perc_positivo:.2f}%')
    print()
    print(f'\033[0;34mForam digitados {num_negativo} valor(es) NEGATIVO')
    print(f'\033[0;35mPercentual de números Negativos: {perc_negativo}%')
    print()
    print(f'Valor máximo digitado : {num_maximo}')
    print(f'Valor mínimo digitado: {num_minimo}')