from PySide2.QtWidgets import *
from PySide2.QtGui import *
import random

class Isen(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setFixedSize(500,300)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.label=QLabel('CSI' )
        self.button = QPushButton ('Changer le cycle')



        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)


        self.button.clicked.connect(self.tirage)

        self.setLayout(self.layout)


    def tirage(self):
        cycles = ['CSI','CIR','BIOST','CENT','BIAST','EST']
        choix = random.choice(cycles)
        print(choix)
        self.label.setText(choix)

if __name__ == '__main__':

    app = QApplication([])
    isen = Isen()
    isen.show()
    app.exec_()
