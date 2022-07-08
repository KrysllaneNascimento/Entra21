# Faça um programa, utilizando for , que peça para o
# usuário inserir um número N e mostre na tela todos
# os números ímpares até N.
num = int(input('Digite um número: '))
print('Número ímpares: ', end='')
for i in range(num + 1):
    if i % 2 != 0:
        print(i, end=' ')

