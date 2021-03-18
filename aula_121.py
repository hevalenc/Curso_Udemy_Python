#aula sobre fazer uma calculadora com o PyQT5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent) #chamar o inicializador da superclasse
        self.setWindowTitle('Calculadora PyQT') #nomear a janela do windows que executará este programa
        self.setFixedSize(400,400) #configurar o tamanho da janela
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit() #configuração do layout da janela, edição das linhas
        self.grid.addWidget(self.display, 0, 0, 1, 5) #tamanho do display: linha = 0, coluna = 0, rowspan = 1, colspan = 5
                                        #os dois primeiros números é para a localização e os outros dois são para o tamanho
        self.display.setDisabled(True) #a janela com a saída dos dados não será editável (display)
        self.display.setStyleSheet(
            '*{backgroud: white; color: #000; font-size: 30px}' #definição de cores e fonte do texto
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding) #os botões serão acomodados com o tamanho da tela

        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''), #limpar o display
            'background: red; color: white; font-weight: 700'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1] #apagar um dígito a esquerda
            )
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(QPushButton(''), 3, 4, 1, 1)

        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(''), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 4, 4, 1, 1,
            self.eval_igual
        )

        self.setCentralWidget(self.cw) #configuração do centro da janela

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None): #método para adicionar os botões
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding) #os botões serão acomodados com o tamanho
                                                                        #da tela
    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_() #executar o código em uma janela do windows