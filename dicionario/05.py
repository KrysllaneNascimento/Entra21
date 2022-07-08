from operator import itemgetter
email = open('email.txt', 'r')
nomes = open('nomes.txt', 'r')
lista1 = nomes.read().splitlines()
lista2 = email.read().splitlines()
dic3 = {}
for i in range(len(lista1)):
    dic3[lista1[i]] = lista2[i]
dicnovo = sorted(dic3.items(), key=itemgetter(1), reverse=True)
for i, dic3 in enumerate(dicnovo):
    print(f'{dic3[0]} = {dic3[1]}')


