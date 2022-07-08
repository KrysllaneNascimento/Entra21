
#EXERCICIO 0001:
#
import PySimpleGUI as sg


layout = [
    [sg.Text('ALUNO', justification='c', font=30, size=(20, 1))],
    [sg.Frame('', [
    [sg.Text('Nome:'), sg.Input(key='name', size=(20, 1), font=30)],
    [sg.Text('Idade:'), sg.Input(key='id', size=(20, 1))],
    [sg.Button('OK'), sg.Combo(['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15'])]

])]


]

janela = sg.Window('Aula', layout)
eventos, valores = janela.read()
#========================================
# sg.theme('SystemDefaulti')
#
# layout = [
#
#     [sg.Text('digite seu nome:'), sg.Input(key='nome', size=(20, 1))],
#     [sg.Text('digite sua turma:'), sg.Input(key='turma', size=(20, 1))],
#     [sg.Text('Matemática:'), sg.Spin(list(range(1, 11)), key='mat')],
#     [sg.Text('Leitura:'), sg.Spin(list(range(1, 11)), key='lei')],
#     [sg.Text('Música:'), sg.Spin(list(range(1, 11)), key='mus')],
#     [sg.Text('Ciências:'), sg.Spin(list(range(1, 11)), key='cie')],
#     [sg.Text('Média'), sg.Text(' ', key='med')],
#     [sg.Button('Calcular')]
#
# ]
# janela = sg.Window('Aula', layout)
# eventos, valores = janela.read()
# while True:
#     eventos, valores = janela.read()
#     if eventos == 'Calcular':
#         med = (valores['mat'] + valores['lei'] + valores['mus'] + valores['cie']) / 4
#         janela['med'].Update(med)

# =============================================================



# theme_name_list = sg.theme_list()
# print(theme_name_list)
# sg.popup('Olá,Mundo')
# sg.popup_ok_cancel('Olá,Mundo')
# sg.popup_notify('Enviado')
#Composição de uma janela:

# layout = [
#     [sg.Text('Olá mundo')]
# ]

# layout = [
#     [sg.Text('Olá,Mundo!')],     #Atenção para a vírgula
#     [sg.Button('OK')]
# ]
#
#

# RESENHA layout = [
#     [sg.Text('Krysllane MaraviLinda')],
#     [sg.Button('VERDADE')]
# ]
# janela = sg.Window('Aula', layout)
# janela.read()

    # [sg.Text('Olá,Mundo!')],     #Atenção para a vírgula
    # [sg.Input()],
    # [sg.Multiline()],
    # [sg.Combo(['Krysllane', 'Lorena'])],
    # [sg.Checkbox('Deficiente?')],
    # [sg.Radio('sim', 'opc'), sg.Radio('nao', 'opc'), sg.Radio('talvez', 'opc')],
    # [sg.Spin(list(range(1, 100)))],
    # [sg.Slider((1, 100))],
    # [sg.Button('OK')],
    # [sg.Image(r'C:\Users\guest01\Downloads\monica.png')],
    # [sg.Text('Olá Mundo')],

# SALVAR VALORES E EVENTOS
# layout = [
#     [sg.Input(key='Nome')],
#     [sg.Button('Salvar')]
# ]
# janela = sg.Window('Aula', layout)
# eventos, valores = janela.read()
# print(eventos)
# print(valores)
# if eventos == 'Salvar':
#     print('Nome salvo')
#     print(valores['Nome'])


# WHILE TRUE
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Slider((1, 100))],
#     [sg.Button('OK')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         print('Nome salvo')
#         print(valores['nome'])
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATUALIZAR VALORES
# layout = [
#     [sg.Text('OLA MUNDO', key='txt')],
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar', key='btn')],
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     print(type(janela))
#     if eventos == 'btn':
#         janela['nome'].Update('PAULO')
#         janela['txt'].Update('PAULO')
#     elif eventos == sg.WINDOW_CLOSED:
#         break


# ATRIBUTOS
# layout = [
#     # [sg.Input(key='nome', default_text='Digite aqui', background_color='Cyan')],
#     # [sg.Button('Salvar')],
#     # [sg.Slider((1.0, 11.0), orientation='h', size=(30, 20), key='slider')],
#     [sg.Text('OLA MUNDO', size=(30, 1), font=30, justification='r')],
#     [sg.Slider((1, 100), enable_events=False, key='slider', orientation='h')],
#     [sg.Button('Salvar')]
#
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela['slider'].Update(range=(1, 10))


# FECHAR JANELA
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button('Salvar')]
#
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     print(eventos)
#     print(valores)
#     if eventos == 'Salvar':
#         janela.close()    #Janela não pode ser mais reaberta
#         break



# REABRIR JANELA
# txtBotao = 'Salvar'
# layout = [
#     [sg.Input(key='nome')],
#     [sg.Button(txtBotao)],
#     [sg.Combo(sg.theme_list(), key='combolista')]
# ]
# janela = sg.Window('Aula', layout)
# while True:
#     eventos, valores = janela.read()
#     if eventos == 'Salvar':
#         # print(sg.theme_list())
#         sg.theme(valores['combolista'])
#         txtBotao = 'ola'
#         janela.close()
#         layout = [
#             [sg.Input(key='nome')],
#             [sg.Button(txtBotao)],
#             [sg.Combo(sg.theme_list())]
#         ]
#         janela = sg.Window('Aula', layout)
#         eventos, valores = janela.read()
#         break










# CÓDIGO ENTRA21
# import getpass
# import json
# # from FuncaoTrabalho import fazer_cadastro, validar, armazenar, preenchimento, salvar, cores
# import PySimpleGUI as sg
# import requests
# import requests
# import json
#
#
#
# def fazer_cadastro(nome, senha):  #ESTABELECER UM PADRÃO PARA CONTAS A SEREM CRIADAS
#     dados = {
#         'usuario_cadastro': nome,
#         'senha_cadastro': senha,
#         'cpf': '',
#         'genero': '',
#         'email': '',
#         'cor': '',
#         'sim': False,
#         'nao': True,
#         'endereco': '',
#         'bairro': '',
#         'dat nasc': '',
#         'wpp': '',
#         'c-email': '',
#         'estadoCivil': '',
#         'cep': '',
#         'estado': '',
#         'cidade': '',
#         'nome completo':''
#     }
#     return dados
#
#
# def validar(usuario, senha):   #VALIDAR USUARIO DIGITADO NA AREA DE LOGIN
#     arq = requests.get('https://trabpysigui-default-rtdb.firebaseio.com/.json')
#     # arq = requests.delete('https://trabpysigui-default-rtdb.firebaseio.com/.json')
#     for i in requests.get('https://trabpysigui-default-rtdb.firebaseio.com/.json').json():
#         if arq.json()[i]['usuario_cadastro'] == usuario and arq.json()[i]['senha_cadastro'] == senha:
#             return True, arq.json()[i], i
#     return False
#
#
# # print(validar('arthur', '123'))
#
#
# def armazenar(dicionario):   #GUARDAR VALORES DO CADASTRO
#     dicionario = json.dumps(dicionario)
#     arq = requests.post('https://trabpysigui-default-rtdb.firebaseio.com/.json', data=dicionario)
#
#
# def preenchimento(janela, valores):    #PREENCHER IFORMAÇÕES NA ÁREA DE INFORMAÇÕES
#     for i in validar(valores['usuario'], valores['senha'])[1]:
#         if i != 'senha_cadastro' and i != 'usuario_cadastro':
#             print(f'{i} CARREGADO')
#             janela[i].Update(validar(valores['usuario'], valores['senha'])[1][i])
#
#
# def salvar(janela, valores):   #SALVAR INFORMAÇÕES
#     for i in validar(valores['usuario'], valores['senha'])[1]:
#         if i != 'senha_cadastro' and i != 'usuario_cadastro':
#             valorNovo = janela[i].get()
#             arq = requests.patch(f'https://trabpysigui-default-rtdb.firebaseio.com/{validar(valores["usuario"], valores["senha"])[2]}/.json', data=json.dumps({i : valorNovo}))
#             print(f'{valorNovo} foi salvo!')
#
# def cores(janela, valores):  #BOTAR CORES CASO HAJA UM ITEM FALTANDO
#     contCaixasVazias = 0
#     for i in validar(valores['usuario'], valores['senha'])[1]:
#         if i != 'senha_cadastro' and i != 'usuario_cadastro':
#             if janela[i].get() == '':
#                 try:
#                     janela[i].Update(background_color='pale violet red')
#                     contCaixasVazias += 1
#                 except:
#                     contCaixasVazias += 1
#             else:
#                 try:
#                     if type(janela[i].get()) != bool:
#                         janela[i].Update(background_color='#dae0e6')
#                 except:
#                     print()
#     return contCaixasVazias
#
#
#
# from time import sleep
# #Layout
# sg.theme('Reddit')
# mostrarSenha = '*'
# cont = 0
# layout = [
#     [sg.Frame('', [[sg.Text('CENTRAL DOS INSCRITOS', justification='c', font='20', pad=20, expand_x=True)],
#     [sg.Text('Nome:', s=(35, 1), justification='l')],
#     [sg.Input(key='usuario', expand_x=True)],
#     [sg.Text('Senha:', s=(35, 1), justification='l')],
#     [sg.Input(key='senha', s=(40, 1), password_char=mostrarSenha), sg.Button('', key='versenha')],
#     [sg.Button('Login',key= 'salvar', expand_x=True)],
#     [sg.Button('Cadastrar', key='cadastro', expand_x=True)],
#     [sg.Text("", key="mensagem")]], pad=30, border_width=4)]
# ]
#
# layout_principal_l = [
#     [sg.Text('CPF', size=(19, 1), justification='c')],
#     [sg.Input(key='cpf', s=(21, 1))],
#     [sg.Text('GENERO', size=(19, 1), justification='c')],
#     [sg.Combo(['Homem', 'Mulher', 'Não Binário', 'Mulher Trans', 'Homem Trans'], s=(19, 1), readonly=True, key='genero')],
#     [sg.Text('EMAIL', size=(19, 1), justification='c')],
#     [sg.Input(key='email', s=(21, 1))],
#     [sg.Text('COR', size=(19, 1), justification='c')],
#     [sg.Combo(['Preto', 'Branco', 'Pardo', 'Amarelo'], s=(19, 1), key='cor', readonly=True)],
#     [sg.Text('ALGUMA DEFICIENCIA?', size=(19, 1), justification='c')],
#     [sg.Radio('sim', 'opc', key='sim'), sg.Radio('nao', 'opc', key='nao', s=(8, 1))],
#     [sg.Text('ENDEREÇO', size=(19, 1), justification='c')],
#     [sg.Input(key='endereco', s=(21, 1))],
#     [sg.Text('BAIRRO', expand_x=True, justification='c')],
#     [sg.Input(key='bairro', s=(21, 1))]
# ]
# layout_principal_r = [
#     [sg.Text('DATA DE NASCIMENTO', size=(18, 1), justification='c')],
#     [sg.Input(key='dat nasc', s=(21, 1))],
#     [sg.Text('WPP', size=(18,1), justification='c')],
#     [sg.Input(key='wpp', s=(21, 1))],
#     [sg.Text('CONFIRM EMAIL', size=(18,1), justification='c')],
#     [sg.Input(key='c-email', s=(21, 1))],
#     [sg.Text('ESTADO CIVIL', size=(18,1), justification='c')],
#     [sg.Combo(['CASADO(A)', 'SOLTEIRO(A)', 'SEPARADO(A)', 'VIUVO(A)'], s=(19, 1), key='estadoCivil', readonly=True)],
#     [sg.Text('CEP', size=(18,1), justification='c')],
#     [sg.Input(key='cep', size=(21,1), enable_events=True)],
#     [sg.Text('ESTADO', size=(18, 1), justification='c')],
#     [sg.Input(key='estado', s=(21, 1))],
#     [sg.Text('CIDADE', size=(18, 1), justification='c')],
#     [sg.Input(key='cidade', s=(21, 1))],
# ]
#
# layout_principal = [
#     [sg.Frame('', [
#         [sg.Text('INSIRA SEUS DADOS')],
#         [sg.Text('NOME COMPLETO', font=18, size=(37, 1), justification='c')],
#         [sg.Input(key='nome completo', size=(37 ,1), font=22, justification='c'), ],
#         [sg.Col(layout_principal_l),sg.Col(layout_principal_r)],
#         [sg.Button('Salvar'), sg.Button('Parar')]
#     ])],
#     ]
# layout_cadastro = [
#     [sg.Frame('',[[sg.Text('Nome'), sg.Input(key='usuario_cadastro')],
#     [sg.Text('Senha'), sg.Input(key='senha_cadastro', password_char='*'), sg.Button('', key='versenha')],
#     [sg.Button('Cadastrar', key='salvar_cadastro')],
#     [sg.Text("", key="mensagem")]])]
#     ]
#
# janela = sg.Window('Tela de Login', layout, element_justification='c', background_color='Blue')
#     #janela
# while True:
#     eventos, valores = janela.read()
#     if eventos == 'versenha':       #Clicou no botao para MOSTRAR senha
#         if janela['senha'].PasswordCharacter == '*':     #Se tiver com *, então ele muda para mostrar sem
#             janela['senha'].Update(password_char='')
#         else:                                            #Senão, quer dizer que ele ja está mostrando as letras, então a senha é ocultada denovo
#             janela['senha'].Update(password_char='*')
#
#     if eventos == 'cadastro':       #Clicou no botao CADASTRO
#         janela_cadastro = sg.Window('Tela de Cadastro', layout_cadastro, element_justification='c', background_color='Blue')
#         while True:
#             eventos_cadastro, valores_cadastro = janela_cadastro.read()
#             #Mesma processo de mostrar senha do código passado
#             if eventos_cadastro == 'versenha':
#                 if janela_cadastro['senha_cadastro'].PasswordCharacter == '*':
#                     janela_cadastro['senha_cadastro'].Update(password_char='')
#                 else:
#                     janela_cadastro['senha_cadastro'].Update(password_char='*')
#
#             if eventos_cadastro == 'salvar_cadastro':
#                 if valores_cadastro['usuario_cadastro'] == '' or valores_cadastro['senha_cadastro'] == '':
#                     print("Informar valor nas duas caixa de texto!")
#                 else:
#                     armazenar(fazer_cadastro(valores_cadastro['usuario_cadastro'], valores_cadastro['senha_cadastro']))
#                     janela_cadastro['mensagem'].update('Usuario cadastrado com sucesso!')
#                     sg.Window.close(janela_cadastro)
#                     break
#             if eventos_cadastro == sg.WINDOW_CLOSED:
#                 break
#
#
#
#
#     elif eventos == 'salvar':                         #Clicou em botao LOGIN
#         try:
#             if validar(valores['usuario'], valores['senha']):
#                 print("Login feito com sucesso!")
#                 janela['mensagem'].update("Login feito com sucesso!")
#                 sg.Window.close(janela)
#                 # janela
#                 janela_principal = sg.Window('Tela de Cadastro', layout_principal, element_justification='c')
#                 # ler os eventos
#
#                 eventos_principal, valores_principal = janela_principal.read(timeout=0)
#                 sg.popup_quick_message('CARREGANDO...', no_titlebar=True)
#                 preenchimento(janela_principal, valores)   #COMECA A PREENCHER COM OS VALORES PADROES OU QUE JA FORAM INFORMADOS
#                 janela_principal.force_focus()
#                 while True:
#                     eventos_principal, valores_principal = janela_principal.read()
#                     # janela_principal['nome completo'].Update(validar(valores['usuario'], valores['senha'])[1]['usuario_cadastro'])
#                     if eventos_principal == 'Salvar':
#                         if cores(janela_principal, valores) >= 1:
#                             sg.popup_quick_message(f'Há {cores(janela_principal,valores)} caixa(s) preenchida(s) errado!', auto_close_duration=5)
#                             continue
#                         else:
#                             sg.popup_quick_message('SALVANDO...', no_titlebar=True)
#                             salvar(janela_principal, valores)
#                             # cores(janela_principal, valores)
#                             print('Dados salvos')
#                             cont += 1
#                             continue
#                     if eventos_principal == 'Parar':
#                         eventos = sg.WINDOW_CLOSED
#                         print('Programa encerrado')
#                         break
#                     if len(janela_principal["cep"].get()) >= 8:    #PREENCHER COM CEP
#                         try:
#                             arq = requests.get(f'https://viacep.com.br/ws/{janela_principal["cep"].get()}/json/')
#                             janela_principal['cidade'].Update(arq.json()['localidade'])
#                             janela_principal['estado'].Update(arq.json()['uf'])
#                             janela_principal['endereco'].Update(arq.json()['logradouro'])
#                             janela_principal['bairro'].Update(arq.json()['bairro'])
#                         except:
#                             print('deu n')
#                 break
#
#             else:
#                 janela['mensagem'].update("Usuario ou Senha incorreta!")
#
#         except:
#             janela['mensagem'].update("Não há nenhum cadastro!")
#
#     if eventos == sg.WINDOW_CLOSED:
#         print('Programa encerrado')
#         break