print("-"*50)
print("CASA DE CÂMBIO".center(50))
print("-"*50)
# dolar, real, euro, libra
moedas = [4.82, 1, 5.17, 6.04]
tipo_moedas = ['Dólares', 'Reais', 'Euros', 'Libras Esterlinas']

entrada = int(input("""
    (0)Dólar
    (1)Real
    (2)Euro
    (3)Libra esterlina
    TENHO: """))

saida = int(input("""
    (0)Dólar
    (1)Real
    (2)Euro
    (3)Libra esterlina
    QUERO: """))

valor_necessario = float(input(f'Quantos {tipo_moedas[saida]} você deseja: '))

print(f'Você precisa de: {valor_necessario/moedas[entrada]*moedas[saida]:.2f} {tipo_moedas[entrada]}')