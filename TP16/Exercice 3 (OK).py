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
        n = 0
        self.button.clicked.connect(self.text)
        n += 1
        self.setLayout(self.layout)

    def closed(self):
        self.close()

    def text(self,n):
        while n<=20 :
            bouttontext = 'click' + str(n)
            self.button.setText(bouttontext)


if __name__ == '__main__':
    app = QApplication([])
    cha = change()
    cha.show()
    app.exec_()
