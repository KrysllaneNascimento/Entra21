# 5. Faça um programa, utilizando for e listas, que pergunte ao usuário quantos produtos ele
# deseja cadastrar, cadastre os produtos e seus respectivos preços em listas separadas e os mostre na tela juntos.
print('Quantos produtos você deseja cadastrar?')
num = int(input('Resposta: '))
print()
print('='*30)
produto = []
preco = []

for i in range(num):
    novo_produto = input(f'Produto {i+1}: ')
    produto.append(novo_produto)
    novo_preco = input(f'Preço R$: ')
    preco.append(novo_preco)
    print()
print('='*30)

for i in range(num):
    print(f'Produto: {produto[i]} - Preço: {preco[i]}')


