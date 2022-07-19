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
# EXERC 004
#
# from math import ceil
#
#
# class BombaCombustivel():
#     def __init__(self, tipo_combust, valor_litro, qtde_combust):
#         self.tipo_combust = tipo_combust
#         self.valor_litro = valor_litro
#         self.qtde_combust = qtde_combust
#
#     def abastecer_Por_Valor(self, valor):
#         total_litro = valor / self.valor_litro
#         dinheiro_bomba = self.qtde_combust * self.valor_litro
#         if self.qtde_combust <= 0:
#             print('Bomba de combustível VAZIA,abasteça em outro lugar')
#             print('=' * 40)
#
#         elif dinheiro_bomba < valor:
#             print(f'Seu carro foi abastecido com {ceil(self.qtde_combust)} litros e faltou {ceil(total_litro - self.qtde_combust)} litros')
#             print('=' * 40)
#
#         else:
#             print(f'Seu carro foi abastecido com {ceil(total_litro)} litros ')
#
#         self.altera_quantcomb(total_litro)
#
#     def abastecer_Por_Litro(self, litro):
#
#         pago = self.valor_litro * litro
#         if self.qtde_combust <= 0:
#             print('Bomba de combustível VAZIA,abasteça em outro lugar')
#             print('='*40)
#         elif self.qtde_combust < litro:
#             print(f'Seu carro foi abastecido com {ceil(self.qtde_combust)} litros e faltou {ceil(litro - self.qtde_combust)} litros')
#             print('=' * 40)
#         else:
#             print(f'Valor total do seu abastecimento:{pago},00 R$')
#         self.altera_quantcomb(litro)
#
#     def altera_Valor(self, litro):
#         self.valor_litro = litro
#
#     def altera_combust(self, combustivel):
#         self.tipo_combust = combustivel
#
#     def altera_quantcomb(self, menos):
#         self.qtde_combust -= menos
#
#
# tipo = input('Tipo de combustível: ')
# valor_li = float(input('Valor do litro: '))
# qtde = int(input('Frentista digite a quantidade de combustivel na bomba: '))
# carro = BombaCombustivel(tipo, valor_li, qtde)
# print('ABASTECER:\n[1] POR LITRO\n[2] POR VALOR A SER PAGO')
# options = int(input('Digite 1 ou 2: '))
# if options == 1:
#     abast_valor = float(input('Insira o valor em R$ que deseja abastecer: '))
#     carro.abastecer_Por_Valor(abast_valor)
#     carro.abastecer_Por_Valor(abast_valor)
#     carro.abastecer_Por_Valor(abast_valor)
# else:
#     abast_valor = int(input('Digite quantos Litros deseja abastecer: '))
#     carro.abastecer_Por_Litro(abast_valor)
#     carro.abastecer_Por_Litro(abast_valor)
#     carro.abastecer_Por_Litro(abast_valor)


#=======================================


#EXERC 005 Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estômago) e pelo menos os métodos comer(),
# verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos
# 3 tres alimentos diferentes e verificando o conteúdo do estômago a cada refeição. Experimente fazer com que um macaco coma o outro.
# É possível criar um macaco canibal?
#alimentos,conteudo bucho,
# class Macaco():
#     def __init__(self, nome):
#         self.nome = nome
#         self.bucho = []
#
#     def comer(self, alimento):
#         self.bucho.append(alimento)
#
#     def __repr__(self):
#         return repr(self.nome)
#
#     def verBucho(self):
#         print(f'{self.__repr__()} comeu {self.bucho}'.replace("'", ' '))
#
#     def digerir(self):
#         self.bucho.pop(0)
#         print(self.bucho)
#
#
# macaco1 = Macaco('Mac1')
# macaco1.comer('laranja')
# macaco1.verBucho()
# macaco1.comer('maçã')
# macaco1.verBucho()
# macaco1.digerir()
# macaco1.comer('pera')
# macaco1.verBucho()
# macaco1.digerir()
#========================================

