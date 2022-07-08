# 4. Faça um programa, utilizando for, que peça ao usuário um número e mostre a sua tabuada,
# enquanto o usuário quiser.
print('='*30)
print('TABUADAS!'.center(30))
print('='*30)
print('Deseja ver uma Tabuáda?[s] ou [n] \n')
laco = input('Resposta: ').upper()
print()
while laco == 'S':
    num = int(input('Tabuada de: \n'))
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
    print('')
    l = input('Deseja ver uma tabuada?[s] ou [n]:').upper()
    if l == 'N':
        break