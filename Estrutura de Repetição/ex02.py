num = int(input('Digite um número: '))
print('-'*30)

cont = 1
multi = 1

while cont <= num:
    multi *= cont
    cont += 1

print(f'{num}! = {multi}')


# from math import factorial
#
# num = int(input('Digite um número:'))
# fatorial = factorial(num)
# print(f'FATORIAL DE {num}: {fatorial}')


