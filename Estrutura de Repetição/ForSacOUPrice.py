valor = float(input('Qual valor deseja financiar? '))
taxa = float(input('Digite o juros mensal do seu empréstimo:'))/100
meses = int(input('Em quantos meses deseja parcelar? '))
tipo = int(input('Deseja amortizar com Tabela [1]SAC ou [2]PRICE?'))

while tipo != 1 and tipo != 2:
    print('Você digitou um valor inválido... Tente novamente')
    tipo = int(input('Deseja amortizar com Tabela [1]SAC ou [2]PRICE?'))

saldo_devedor = valor
print('-'*80)
print('\033[1mN°       |    VALOR PARCELA  |   AMORTIZAÇÃO   |    JUROS  |   SALDO DEVEDOR')
print('-'*80)
if tipo == 1:
    amortizacao = valor / meses
    for i in range(meses):
        juros = (saldo_devedor * taxa)
        saldo_devedor -= amortizacao
        valor_parcela = amortizacao + juros
        print(f' {i+1}       |    R${valor_parcela:.2f}      |  R${amortizacao:2f}    |  R${juros:.2f}   |  R${saldo_devedor:.2f}'.center(30))
        print('-'*80)
elif tipo == 2:
    valor_parcela = valor / (((1+taxa)**meses-1) / ((1+taxa)**meses * taxa))
    for i in range(meses):
        juros = saldo_devedor * taxa
        amortizacao = valor_parcela - juros
        saldo_devedor -= amortizacao
        print(f' {i+1}       |    R${valor_parcela:.2f}      |  R${amortizacao:.2f}    |  R${juros:.2f}   |  R${saldo_devedor:.2f}'.center(30))
        print('-' * 80)