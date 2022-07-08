a = open('cA', 'r')
b = open('cB', 'r')
todos = open('ctodos', 'r')
lista1 = a.read().splitlines()
lista2 = b.read().splitlines()
lista3 = todos.read().splitlines()

total_eleitor = 100
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

v_dois = set1.intersection(set2)



print(f'Votos do candidato A: {len(lista1)}')
print(f'Votos do candidato B: {len(lista2)}')
print(f'Pessoas que votaram nos 2 candidatos: {len(v_dois)}')
print(f'Não votaram: {total_eleitor - len(set3)}')
print(f'Novo vencedor: B')