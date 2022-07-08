nome = (input('Digite seu nome: '))
n1 = int(input('Digite nota 1: '))
n2 = int(input('Digite nota 2: '))
n3 = int(input('Digite nota 3: '))
n4 = int(input('Digite nota 4: '))
m= (n1 + n2+ n3 +n4) / 4
if m >= 7:
    print(f'{nome},você foi APROVADO')
elif m >= 5:
    print(f'{nome}, você ficou em exame')
else:
    print(f'{nome},estude mais !')


