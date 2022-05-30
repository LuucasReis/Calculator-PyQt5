from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
import sys

class Calculadora(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora - By Lucas Reis")
        self.setFixedSize(400,400)
        self.cenwid= QWidget()
        self.grid= QGridLayout(self.cenwid)

        
        self.display = QLineEdit()
        self.grid.addWidget(self.display,0,0,1,5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            "*{background: white; color: black; font-size: 30px;}"
        )

        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        #Adicionando botões da primeira coluna
        self.add_numeros(QPushButton("7"),1,0,1,1)
        self.add_numeros(QPushButton("8"),1,1,1,1)
        self.add_numeros(QPushButton("9"),1,2,1,1)
        self.add_numeros(
            QPushButton("+"),1,3,1,1,
            estilo="background: #095177; color: white; font-weight: 700;"
            )
        self.add_numeros(
            QPushButton("C"),1,4,1,1,
            lambda: self.display.setText(''),
            "background: #d90d0d; color: white; font-weight: 700;"
            )

        #Adicionando botões da segunda colona
        self.add_numeros(QPushButton("4"),2,0,1,1)
        self.add_numeros(QPushButton("5"),2,1,1,1)
        self.add_numeros(QPushButton("6"),2,2,1,1)
        self.add_numeros(
            QPushButton("-"),2,3,1,1,
            estilo="background: #095177; color: white; font-weight: 700;"
            )
        self.add_numeros(
            QPushButton("<-"),2,4,1,1,
            lambda: self.display.setText(self.display.text()[:-1]),
            "background: #ff6600; color: white; font-weight: 700;"
                
                )

        #Adicionando botões da terceira coluna
        self.add_numeros(QPushButton("1"),3,0,1,1)
        self.add_numeros(QPushButton("2"),3,1,1,1)
        self.add_numeros(QPushButton("3"),3,2,1,1)
        self.add_numeros(
            QPushButton("/"),3,3,1,1,
            estilo="background: #095177; color: white; font-weight: 700;"
            )
        self.add_numeros(QPushButton(""),3,4,1,1)

        #Adicionando botões da quarta coluna
        self.add_numeros(QPushButton(""),4,0,1,1)
        self.add_numeros(QPushButton("0"),4,1,1,1)
        self.add_numeros(QPushButton("."),4,2,1,1)
        self.add_numeros(
            QPushButton("*"),4,3,1,1,
            estilo="background: #095177; color: white; font-weight: 700;"
        )
        self.add_numeros(
            QPushButton("="),4,4,1,1,
            self.f_igual,
            "background: #009900; color: white; font-weight: 700;"
            )

        self.setCentralWidget(self.cenwid)

    def add_numeros(self, btn, row, colunm, rowspan, colspan, f=None, estilo=None):
        self.grid.addWidget(btn,row,colunm,rowspan,colspan)
        if not f:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text()+ btn.text()
                )
            )
        else:
            btn.clicked.connect(f)

        if estilo:
            btn.setStyleSheet(estilo)


        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    
    def f_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )

        except Exception as e:
            self.display.setText("Conta inválida")
            

        



if __name__=="__main__":
    qt = QApplication(sys.argv)
    calc= Calculadora()
    calc.show()
    qt.exec_()