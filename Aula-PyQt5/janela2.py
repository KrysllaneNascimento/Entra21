from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def click():
    janela.label.setText()


app = QApplication([])
janela = uic.loadUi('janela.ui')
janela.pushButton.clicked.connect(click)