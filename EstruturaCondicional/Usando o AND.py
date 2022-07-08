nome = input('Digite o seu nome: ')
cargo = input('Digite o seu cargo: (1) Professor (2) Coordenador (3) Zelador: ')
salario = float(input('Digite o seu Salário Atual: '))
salario_novo = salario * 1.1
bonificacao = salario_novo * 0.05

if salario_novo < 1999:
    irrf = 0
elif salario_novo < 2967:
    irrf = salario_novo * 0.075
elif salario_novo < 3938:
    irrf = salario_novo * 0.15
elif salario_novo < 4987:
    irrf = salario_novo * 0.225
else:
    irrf = salario_novo * 0.275

salario_liquido = salario_novo - irrf + bonificacao

print(f'COLABORADOR: {nome.upper()}')
if cargo == '1':
    print('CARGO: PROFESSOR')
elif cargo == '2':
    print('CARGO: COORDENADOR')
else:
    print('CARGO: ZELADOR')

print(f'Salário Novo: {salario_novo:.2f}')
print(f'Bonificação: {bonificacao:.2f}')
print(f'IRRF: {irrf:.2f}')
print(f'Salário líquido: {salario_liquido:.2f}')