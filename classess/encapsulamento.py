# #encapsular : __exemplo(impede que você acesso um elemento diretamente, apenas da para acessar através da função)
# class Conta:
#     def __init__(self, agencia, conta, saldo=0.0):
#         self.agencia = agencia
#         self.conta = conta
#         self.__saldo = saldo
#
#     def depositar(self, valor):
#         self.__saldo += valor
#         self.ver_saldo()
#         self.__mensagem()
#
#     def ver_saldo(self):
#         print(self.__saldo)
#
#     def __mensagem(self):
#         print(f'Bom dia, seu depósito foi feito')
#
#
# c1 = Conta(3365, '1234-5')
# c1.depositar(200)
from math import ceil


class Carro:
    def __init__(self, consumo, nivel_comb=0):
        self.__consumo = consumo
        self.__nivel_comb = nivel_comb
        self.capacidade = self.__consumo*self.__nivel_comb

    def adicionarGasolina(self, qtde):
        self.__nivel_comb += qtde
        self.capacidade = self.__consumo * self.__nivel_comb
        print(self.capacidade)

    def andar(self, km):
        if km <= self.capacidade:
            print(f'Você andou {km}')
            self.__nivel_comb -= km/self.__consumo
        else:
            print('Você não tem combustivel suficiente')

    def obterGasolina(self):
        print(f'Você tem no tanque {self.__nivel_comb} litros')


carro = Carro(15)
carro.adicionarGasolina(50)
carro.andar(100)
carro.andar(50)
carro.obterGasolina()









