# class Bola:
#     def __init__(self, cor, circunf, material):
#         self.cor = cor
#         self.circunf = circunf
#         self.material = material
#
#     def trocaCor(self, novacor):
#         self.cor = novacor
#
#     def mostraCor(self):
#         print(f'Nova cor {self.cor}')
#
#
# cores = Bola('azul', 52, 'plastico')
# cores.trocaCor('rosa')
# cores.mostraCor()
# ===============
# class Quadrado:
#     def __init__(self, lado):
#         self.lado = lado
#
#     def MudaLado(self, l):
#         self.lado = l
#
#     def NovoValor(self):
#         print(f'Novo valor do lado:{self.lado}')
#         print(f'ÁREA: {self.lado*self.lado}')
#
#
# prin = Quadrado(6)
# novo = int(input('Digite um novo valor do lado: '))
# prin.MudaLado(novo)
# prin.NovoValor()
# ============
# class Retangulo:
#     def __init__(self, compr, larg):
#         self.ladoA = compr
#         self.ladoB = larg
#
#     def mudaA(self, com):
#         self.compr = com
#
#     def mudaB(self, lag):
#        self.larg = lag
#
#     def retornaValor(self):
#         print(f'Novo valor do Comprimento:{self.larg} e Altura:{self.compr}')
#
#     def calculaArea(self):
#         print(f'Valor da área = {self.compr*self.larg}')
#
#     def perimetro(self):
#         print(f'Valor do perimetro:{self.larg*2 + self.compr*2}')
#
#
# todos = Retangulo(4, 4)
# muda = int(input('Novo valor do comprimento: '))
# mudb = int(input('Novo valor da largura: '))
# todos.mudaA(muda)
# todos.mudaB(mudb)
# todos.calculaArea()
# todos.perimetro()
#
# =====
# (Altura, diametro,volume)
#Material = de alumino , plastico
##Métodos(funcionalidades) = abrir, beber, esvaziar, amassar, retirar lacre, e descartar
#altura = 	12.22 cm
#diâmetro = 52 mm
# # volume = 350 ml
# class Lata:
#     def __init__(self, altura, diametro, volume, material='aluminio', rotulo='coca'):
#         self.altura = altura
#         self.diametro = diametro
#         self.volume = volume
#         self.material = material
#         self.rotulo = rotulo
#         self.lacre = True
#         self.amassada = False
#         self.descartada = False
#         self.aberta = False
#
#     def abrir(self):
#         if self.aberta:
#             print('Já está aberta, bocó')
#         else:
#             print('Lata foi aberta com sucesso')
#             self.aberta = True
#
#     def beber(self, quantidade):
#         if not self.aberta:
#             print('Lata ainda está fechada')
#         elif quantidade > self.volume:
#             print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
#             self.volume = 0
#         else:
#             self.volume -= quantidade
#             print(f'Você bebeu {quantidade}, e na lata ainda resta {self.volume}')
#
#     def esvaziar(self):
#         if not self.aberta:
#             print('Não da para esvaziar com a lata fechada')
#         else:
#             print('Lata vazia')
#             self.volume = 0
#
#     def amassar(self):
#         if not self.amassada and self.volume == 0:
#             print('Lata amassada')
#             self.amassada = True
#         else:
#             print('Não da pra amassar')
#
#     def retirar_lacra(self):
#         if not self.lacre:
#             self.lacre = False
#             print('Lacre retirado')
#         else:
#             print('Não tinha lacre')
#     def descartar(self):
#         if self.descartada:
#             print('Não pode descartar o que já está descartado')
#         elif self.amassada:
#             print('Descartada no lixeiro amarelo')
#             self.descartada = True
#
#         else:
#             print('Primeiro amasse a lata')
#
# l1 = Lata(12.22, 5.2, 350)
# l1.abrir()
# l1.beber(300)
# l1.esvaziar()
# l1.amassar()
# l1.retirar_lacra()
# l1.descartar()
# l1.abrir()Lata foi aberta com sucesso
# l1.abrir()Já está aberta, bocó
# =====
# (Altura, diametro,volume)
#Material = de alumino , plastico
##Métodos(funcionalidades) = abrir, beber, esvaziar, amassar, retirar lacre, e descartar
#altura = 	12.22 cm
#diâmetro = 52 mm
# # volume = 350 ml
# class Lata:
#     def __init__(self, altura, diametro, volume, material='aluminio', rotulo='coca'):
#         self.altura = altura
#         self.diametro = diametro
#         self.volume = volume
#         self.material = material
#         self.rotulo = rotulo
#         self.lacre = True
#         self.amassada = False
#         self.descartada = False
#         self.aberta = False
#
#     def abrir(self):
#         if self.aberta:
#             print('Já está aberta, bocó')
#         else:
#             print('Lata foi aberta com sucesso')
#             self.aberta = True
#
#     def beber(self, quantidade):
#         if not self.aberta:
#             print('Lata ainda está fechada')
#         elif quantidade > self.volume:
#             print(f'Você bebeu {self.volume}, e ainda faltou {quantidade-self.volume}')
#             self.volume = 0
#         else:
#             self.volume -= quantidade
#             print(f'Você bebeu {quantidade}, e na lata ainda resta {self.volume}')
#
#     def esvaziar(self):
#         if not self.aberta:
#             print('Não da para esvaziar com a lata fechada')
#         else:
#             print('Lata vazia')
#             self.volume = 0
#
#     def amassar(self):
#         if not self.amassada and self.volume == 0:
#             print('Lata amassada')
#             self.amassada = True
#         else:
#             print('Não da pra amassar')
#
#     def retirar_lacra(self):
#         if not self.lacre:
#             self.lacre = False
#             print('Lacre retirado')
#         else:
#             print('Não tinha lacre')
#     def descartar(self):
#         if self.descartada:
#             print('Não pode descartar o que já está descartado')
#         elif self.amassada:
#             print('Descartada no lixeiro amarelo')
#             self.descartada = True
#
#         else:
#             print('Primeiro amasse a lata')
#
# l1 = Lata(12.22, 5.2, 350)
# l1.abrir()
# l1.beber(300)
# l1.esvaziar()
# l1.amassar()
# l1.retirar_lacra()
# l1.descartar()
# l1.abrir()Lata foi aberta com sucesso
# l1.abrir()Já está aberta, bocó
