#HERANÇA EM CLASSES: Puxa as funcionalidades e atributos da class mãe
class Veiculo:
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo):
        self.cor = cor
        self.lugares = lugares
        self.qtde_pneus = qtd_pneus
        self.tipo_motor = tipo_motor
        self.valor = valor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print('Acelerou')

    def frear(self):
        print('Freou')

    def ligar(self):
        print('Ligou')

    def desligar(self):
        print('Desligou')


class Moto(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.empinada = empinada

    def empinar(self):
        if self.empinada:
            print('Já esta empinada')
        else:
            print('EMPINAAA')
            self.empinada = True

    def desempinar(self):
        self.empinada = False


#Criar uma classe herdeira carro e outra busão
#As 2 classes novas precisam ter 2 métodos novos e 2 atributos novos cada

class Carro(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, embreagem=False, ar=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.embreagem = embreagem
        self.ar = ar

    def troca_marcha(self):
        if not self.embreagem:
            print('APERTE A EMPREAGEM PARA TROCAR DE MARCHA')
            self.embreagem = True
        else:
            print('EMBREAGEM APERTADA,Pode trocar de marcha!')

    def liga_ar(self):
        if self.ar:
            print('Ar ja está ligado')
        else:
            print('Ar foi ligado')
            self.ar = True

    def desliga_ar(self):
        if not self.ar:
            print('Ar já está desligado')
        else:
            print('Ar desligado')
            self.ar = False








