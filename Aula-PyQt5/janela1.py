from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 300

        self.largura = 800
        self.altura = 600

        self.titulo = 'Primeira Janela'

        botao1 = QPushButton('botao1', self)
        botao1.move(150, 200)
        botao1.resize(100, 80)
        botao1.setStyleSheet('QPushButton {background-color: blue;font:bold;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)
        botao2.move(400, 200)

        botao2 = QPushButton('botao2', self)
        botao2.resize(100, 80)
        botao2.setStyleSheet('QPushButton {background-color: purple;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)

        self.label1 = QLabel(self)
        self.label1.setText('Olá Mundoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        self.label1.move(200, 100)
        self.label1.resize(200, 20)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label1.setText('O botão 1 foi pressionado')
        self.label1.setStyleSheet('QLabel {font-size: 15px;font:bold}')

    def botao2_click(self):
        self.label1.setText('O botão 2 foi pressionado')
        self.label1.setStyleSheet('QLabel {font-size: 15px;font:bold}')



aplicacao = QApplication([])
janela = Janela()
aplicacao.exec()
