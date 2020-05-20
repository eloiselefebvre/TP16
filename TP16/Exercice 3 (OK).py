from PySide2.QtWidgets import *
from PySide2.QtGui import *

class change(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle('IHM')
        self.button = QPushButton('Changer mon texte !')

        self.layout.addWidget(self.button)
        #self.button.clicked.connect(self.closed)
        self.button.clicked.connect(self.text)
        self.setLayout(self.layout)

    def closed(self):
        self.close()

    def text(self):
        n = 0
        while n<=20 :
            bouttontext = 'click' + str(n)
            self.button.setText(bouttontext)
            n += 1

if __name__ == '__main__':
    app = QApplication([])
    cha = change()
    cha.show()
    app.exec_()
