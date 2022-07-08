lista1 = list(range(5, 11))
lista2 = [3, 5, 7, 9, 3]

set1 = set(lista1)
set2 = set(lista2)

print(set1)
print(set2)

# if len(lista2) == len(set2):
#     print('sem duplicadas')
# else:
#     print('duplicadas')

#Juntar 2 sets:
print(f'Union {set2.union(set1)}')
#Valores em comum em 2 sets
print(f'Interseção {set2.intersection(set1)}')
#Valores que são diferente entre os 2 sets
print(f'Diferença {set2.difference(set1)}')
#Ao contrário da intersecção:
print(f'Diferença simétrica {set2.symmetric_difference(set1)}')

#Verificar se um item está no set
# if 9 in set2:
#     print('encontrei')

#Adicionar itens ao set
set2.add(25)
set1.add(14)
print(set1)
print(set2)

#Adicionar uma lista nova ou tupla a um set
tupla1 = (3, 5, 13, 290)
lista3 = [260, 220, 240]
set2.update(tupla1)
print(set2)
set2.update(lista3)
print(set2)

#Apagar um item -Remove( se não tiver o item ira dá KeyError)
# set2.add(200)
# print(set2)
# set2.remove(200)
# print(set2)

#Apagar um item- discard(mesmo se não houver um item não irá da erro)
# set2.add(200)
# print(set2)
# set2.discard(230)
# print(set2)

#Apagar 1° item -pop
# print(set2)
# set2.pop()
# print(set2)

#limpar set
# set2.clear()

#laço no set
for i in set2:
    print(i, end=' ')
