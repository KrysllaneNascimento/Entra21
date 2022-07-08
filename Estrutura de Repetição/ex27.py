nome = input('Digite seu nome completo: ').upper()
nomediv = nome.split()
print(f'Primeiro nome:{nomediv[0]}')
print(f'Último nome:{nomediv[len(nomediv)-1]}')
