# Crie um programa que simule as operações básicas de um banco: Todas as opções devem funcionar.
# Simular que existam 3 contas diferentes, e cada conta só é acessada caso seja apresentada a senha correta.
# a.  	Consultar saldo
# b.  	Pagar conta
# c.   	Depositar na conta
# d.  	Saque
# e.  	Sair
# f.   	O programa só deve se encerrar quando for selecionada  a opção SAIR.

print('\033[1;34mCOOPERATIVA UNIDOS DO DINHEIRO'.center(50))
conta1 = input('\033[1;31mDefina a senha da sua Conta Investimento: ')
print('='*40)
conta2 = input('\033[1;32mDefina a senha da sua Conta Trabalho: ')
print('='*40)
conta3 = input('\033[1;33mDefina a senha da sua Conta Doação: ')
print('='*40)
print('\033[1;35mDeseja fazer alguma transação na sua conta?[s] ou [n] ')
laco = input('\033[1;31mResposta: ').upper()
repeticao = ''

while laco == 'S':
    cont = int(input('\033[0;32mDeseja fazer transação na sua Conta: 1.Investimento, 2.Trabalho ou 3.Doação: '))
    if cont == 1:
        senha = input('\033[1;31mDigite a senha da sua 1° Conta: ')
        if senha != conta1:
            print('Senha incorreta,revise seus dados')
    if cont == 2:
        senha = input('\033[0;32mDigite a senha da sua 2° Conta: ')
        if senha != conta2:
            print('Senha incorreta,revise seus dados')
    if cont == 3:
        senha = input('\033[1;32mDigite a senha da sua 3° Conta: ')
        if senha != conta1:
            print('Senha incorreta,revise seus dados')
    else:
        print('\033[0;35ma.  Consultar saldo\nb.  Pagar conta\nc.  Depositar na conta\nd.  Saque\ne.  Sair')
        op = input('Digite sua resposta: ')
        if op == 'a' and cont == 1:
            saldo = 1000
            print(f'\033[0;32mSeu saldo é : {saldo}')
        elif op == 'b' and cont == 1:
            saldo = 1000
            pagar = int(input('\033[1;32mDigite o valor à pagar: '))
            novo_saldo = saldo - pagar
            print(f'\033[0;34mTRANSAÇÃO EFETUADA COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'c' and cont == 1:
            saldo = 1000
            deposito = int(input('Valor que deseja depositar: '))
            novo_saldo = saldo + deposito
            print(f'0;32mPIX RECEBIDO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'd' and cont == 1:
            saldo = 1000
            saque = int(input('Saque: '))
            novo_saldo = saldo - saque
            print(f'SAQUE EFETUADO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')

        elif op == 'a' and cont == 2:
            saldo = 2000
            print(f'Seu saldo é : {saldo}')
        elif op == 'b' and cont == 2:
            saldo = 2000
            pagar = int(input('Digite o valor à pagar: '))
            novo_saldo = saldo - pagar
            print(f'TRANSAÇÃO EFETUADA COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'c' and cont == 2:
            saldo = 2000
            deposito = int(input('Valor que deseja depositar: '))
            novo_saldo = saldo + deposito
            print(f'PIX RECEBIDO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'd' and cont == 2:
            saldo = 2000
            saque = int(input('Saque: '))
            novo_saldo = saldo - saque
            print(f'SAQUE EFETUADO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')

        elif op == 'a' and cont == 3:
            saldo = 3000
            print(f'Seu saldo é : {saldo}')
        elif op == 'b' and cont == 3:
            saldo = 3000
            pagar = int(input('Digite o valor à pagar: '))
            novo_saldo = saldo - pagar
            print(f'TRANSAÇÃO EFETUADA COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'c' and cont == 3:
            saldo = 3000
            deposito = int(input('Valor que deseja depositar: '))
            novo_saldo = saldo + deposito
            print(f'PIX RECEBIDO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')
        elif op == 'd' and cont == 3:
            saldo = 3000
            saque = int(input('Saque: '))
            novo_saldo = saldo - saque
            print(f'SAQUE EFETUADO COM SUCESSO!\nNOVO SALDO: {novo_saldo}')

        elif op == 'e' and cont == 1:
            print('LOGIN ENCERRADO')
            break
        elif op == 'e' and cont == 2:
            print('LOGIN ENCERRADO')
            break
        elif op == 'e' and cont == 3:
            print('LOGIN ENCERRADO')

        repeticao = input('Deseja fazer uma nova Transaçaõ?  [s] ou [n]:')
        if repeticao == 's':
            print('\033[0;35ma.  Consultar saldo\nb.  Pagar conta\nc.  Depositar na conta\nd.  Saque\ne.  Sair')
            op = input('Digite sua resposta: ')
        elif repeticao == 'N':
            break
        else:
            print('Opção digitada incorreta,revise seus dados.')








