from PySide2.QtWidgets import *
from PySide2.QtGui import *

class change(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle('IHM')
        self.button = QPushButton('Changer mon texte !')
        self.text = QTextEdit('affichage')
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        #self.button.clicked.connect(self.closed)
        self.setLayout(self.layout)
        self.n = 1
        #self.button.clicked.connect(self.buttonchange)
        #self.button.clicked.connect(self.textchange)
        self.button.clicked.connect(self.totalchange)

    #def closed(self):
    #    self.close()

    #def buttonchange(self):
    #    newtext = 'click' + str(self.n)
    #    self.button.setText(newtext)
    #    self.n += 1


    #def textchange(self):
    #    newtext = 'click' + str(self.n)
    #    self.text.setText(newtext)
    #    self.n += 1

    def totalchange(self):
        newtext = 'click' + str(self.n)
        self.text.setText(newtext)
        self.button.setText(newtext)
        self.n += 1


if __name__ == '__main__':
    app = QApplication([])
    change = change()
    change.show()
    app.exec_()


