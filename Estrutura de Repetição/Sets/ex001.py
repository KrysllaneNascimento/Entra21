antigo = open('cnpjantigo.txt', 'r')
novo = open('cnpjnovo.txt', 'r')
todos = open('todos.txt', 'r')
lista1 = antigo.read().splitlines()
lista2 = novo.read().splitlines()
lista3 = todos.read().splitlines()

setantigo = set(lista1)
setnovo = set(lista2)
setodos = set(lista3)

ContUnico = 0
set4 = set()
for i in lista3:
    if lista3.count(i) > 1:
        set4.add(i)
    else:
        ContUnico += 1


print(f'Total de CNPJ cadastrados: {len(lista3)}')
print(f'Total de CNPJ únicos cadastrados: {len(setodos)}')
print(f'Total de CNPJ repetidos removidos: {len(lista3) - len(setodos)}')
print(f'Total de duplicados: {len(set4)}')
print(f'Itens a remover para não ter duplicados: {(len(lista3) - len(setodos))-ContUnico} ')







