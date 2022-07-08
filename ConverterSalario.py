# -Entradas de dados
# --Variaveis
# -Regras
# -Saídas

taxaNovoSalario = 1.1
taxaBonificao = 0.05
taxaIRF = 0

nome = input('Digite seu nome: ')
numeroCargo = int(input('Digite o número do seu cargo [1-Professor,2-Coodernador,3-Zelador]: '))

if numeroCargo <= 0 or numeroCargo > 3:
    print('Número do Cargo INCORRETO')
else:
    salarioAtual = int(input('Digite seu salário:'))

    novoSalarioBruto = salarioAtual * taxaNovoSalario
    bonificacao = novoSalarioBruto * taxaBonificao

    if novoSalarioBruto < 1990:
        taxaIRF = 0
    elif novoSalarioBruto < 2967:
        taxaIRF = 0.075
    elif novoSalarioBruto < 3983:
        taxaIRF = 0.15
    elif novoSalarioBruto < 4987:
        taxaIRF = 0.225
    else:
        taxaIRF = 0.275

    valorIRF = novoSalarioBruto * taxaIRF
    novoSalarioLiquido = (novoSalarioBruto + bonificacao) - valorIRF

    cargo = ''
    if numeroCargo == 1:
        cargo = "Professor"
    elif numeroCargo == 2:
        cargo = "Coordenador"
    else:
        cargo = "Zelador"

    mensagemIRF = f'{valorIRF} reais'
    if valorIRF == 0:
        mensagemIRF = 'ISENTO DE IMPOSTO DE RENDA'

    print(f'\nColaborador: {nome.upper()}')
    print(f'Cargo: {cargo.upper()}')
    print(f'Novo Salário Bruto: {novoSalarioBruto} reais')
    print(f'Bonificação {bonificacao} reais')
    print(f'IRF: {mensagemIRF}')
    print(f'Salário Líquido: {novoSalarioLiquido} reais')