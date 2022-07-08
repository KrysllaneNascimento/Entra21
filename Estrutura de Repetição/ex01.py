cont = 0
num = int(input('Digite um número:'))
print('-'*30)
print('TABUÁDA'.center(30))
print('-'*30)
while cont < 10:

    cont += 1
    multi = num * cont
    print(f'{num} x {cont} = {multi}'.center(10))

