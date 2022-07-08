# 3. Faça um programa, utilizando for e listas/append, que peça o nome de três mulheres e
# três homens e mostre na tela três duplas compostas por um homem e uma mulher.

mulher = []
homem = []

for i in range(1, 4):

    novo_mulher = input(f'Mulher {i}: ')
    mulher.append(novo_mulher)
print()
print(f'Mulheres: {mulher}\n')

for i in range(1, 4):
    novo_homem = input(f'Homem {j}:')
    homem.append(novo_homem)

print(f'Homens: {homem}')
print()

for i in range(3):
    print(f'Dupla: {mulher[i]} e {homem[i]}')


