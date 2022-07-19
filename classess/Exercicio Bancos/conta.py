from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, nome, saldo=0):
        self.nome = nome
        self.agencia = agencia
        self.numero = numero
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        print(valor)

    @abstractmethod
    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo:.2f}')


class Conta_corrente(Conta):
    def __init__(self, agencia, numero, nome,saldo, limite=200):
        super().__init__(agencia, numero, nome, saldo)
        self.__limite = limite
        self.__saldo = saldo

    def sacar(self, valor):
        if valor > self.__saldo + self.__limite:
            print('Saldo insuficiente*')
        else:
            self.__saldo -= valor
            print('SAQUE REALIZADO-')

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo}')


class Conta_poupanca(Conta):
    def __init__(self, agencia, numero, nome, saldo):
        super().__init__(agencia, numero, nome, saldo)
        self.__saldo = saldo

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente#')
        else:
            self.__saldo -= valor
            print('SAQUE REALIZADO--')
        self.exibir_saldo()

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo}')


c1 = Conta_corrente(123123123, 123123132, 'jonas', 1000)
c1.sacar(1100)
c2 = Conta_poupanca(1231231, 1231231, 'Jonas', 1000)
c2.sacar(1100)








