from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, especie, kilos, habitat, alimentacao=False):

        self.alimentacao = alimentacao
        self.kilos = kilos
        self.habitat = habitat
        self.especie = especie
        self.tipos_alim = ['Carne', 'Vegetais', 'Vegatais e Carne']

    @abstractmethod
    def tipo_animal(self, tipo):
        self.especie = tipo

    def comer(self, tipo):
        if self.alimentacao:
            print(f'{self.especie} já está comendo')
            return
        else:
            print(f'{self.especie} come {self.tipos_alim[tipo]}')
            self.alimentacao = True

    def ambiente(self, lugar):
        if lugar == 0:
            self.habitat = 'Terra'
            print(f'{self.especie} vive na {self.habitat}')
        elif lugar == 1:
            self.habitat = 'Mar'
            print(f'{self.especie} vive no {self.habitat}')
        else:
            self.habitat = 'Céu'
            print(f'{self.especie} Voa no {self.habitat}')

    def peso(self, kg):
        if kg <= 10:
            self.kilos = 'animal de Pequeno porte'
            return print(f'{self.especie} {self.kilos}')
        elif kg <= 25:
            self.kilos = 'animal de Médio porte'
            return print(f'{self.especie} {self.kilos}')
        else:
            self.kilos = 'animal de Grande porte'
            return print(f'{self.especie} {self.kilos}')


# espec = input('Qual é o animal: ')
# print('TIPO ALIMENTAR:\n[0]CARNÍVORO\n[1]HERBIVORO\n[2]ONIVORO')
# alimento = int(input('Resposta: '))
# print('HABITAT:\n[0]Terrestre\n[1]Aquático\n[2]Aéreos')
# habit = int(input('Resposta: '))
# peso = int(input('Peso do animal em KG: '))
#
# animal = Animal('girafa', 60, 'terra')
# animal.tipo_animal(espec)
# animal.comer(alimento)
# animal.ambiente(habit)
# animal.peso(peso)


class Cachorro(Animal):
    def __init__(self, especie, porte, habitat, garras=False):
        super().__init__(especie, porte, habitat)
        self.garras = garras

    def garra(self):
        if self.habitat == 1:
            print(f'{self.especie} NÃO POSSUI GARRAS')
        else:
            print(f'{self.especie} POSSUI GARRAS')
            self.garras=True

    def tipo_animal(self, tipo):
        print(f'{tipo} é muito fofinhooo')


a = Cachorro('peixe', 25, 1)
a.garra()
a.tipo_animal('gato')





