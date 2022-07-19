#@abstractmethod - Quando vc quer que obrigatoriamente uma def seja solicitada na class filha

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome, especie, habitat):
        self.nome = nome
        self.especie = especie
        self.habitat = habitat

    @abstractmethod
    def pedir_comida(self):
        return True

    def comer(self):
        print(f'{self.nome} comeu')

    @staticmethod
    def nascar():
        print('nasceu')

    @classmethod
    def morrer(cls):
        print('morreu')


class Felinos(Animal):
    def __init__(self, nome, especie, habitat, garras, orelhas):
        super().__init__(nome, especie, habitat)
        self.garras = garras
        self.orelhas = orelhas

    def pedir_comida(self):
        print('Miauuu')


gato = Felinos('Jinx', 'Ccahorro', 'SEILA', True, 2)
gato.pedir_comida()
