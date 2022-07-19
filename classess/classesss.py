class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')


a2 = Cliente('JOJO', 40)
a1 = Aluno('Marei', 54)
a1.falar()
a1.estudar()
a2.falar()
a2.comprar()

