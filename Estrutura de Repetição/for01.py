# 1. Faça um programa, utilizando for, que permita
# o usuário fazer três contas de subtração.

print('OPERAÇÃO - SUBTRAÇÃO!')
print()
print('='*30)

for i in range(1, 4):
    print(f'Conta {i}')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    sub = num1 - num2
    print(f'{num1} - {num2} = {sub}')
    print('='*30)