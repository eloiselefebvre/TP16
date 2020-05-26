from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Calculator(QWidget) :

    def __init__(self):

        QWidget.__init__(self)
        self.setWindowTitle('Calculator')
        self.setFixedSize(300,300)
        self.layout1 = QGridLayout()
        self.align = Qt.Alignment()
        self.line = QLineEdit()

        self.C = QPushButton('C')
        self.CE = QPushButton('CE')

        self.sept = QPushButton('7')
        self.huit = QPushButton('8')
        self.neuf = QPushButton('9')
        self.slash = QPushButton('/')

        self.quatre = QPushButton('4')
        self.cinq = QPushButton('5')
        self.six = QPushButton('6')
        self.etoile = QPushButton('*')

        self.un = QPushButton('1')
        self.deux = QPushButton('2')
        self.trois = QPushButton('3')
        self.moins = QPushButton('-')

        self.zero = QPushButton('0')
        self.virgule = QPushButton(',')
        self.egal = QPushButton('=')
        self.plus = QPushButton('+')

        self.layout1.addWidget(self.line,1,1,1,4)
        self.layout1.addWidget(self.C,2,1,1,2,self.align)
        self.layout1.addWidget(self.CE,2,3,1,2,self.align)

        self.layout1.addWidget(self.sept,3,1,1,1,self.align)
        self.layout1.addWidget(self.huit,3,2,1,1,self.align)
        self.layout1.addWidget(self.neuf,3,3,1,1,self.align)
        self.layout1.addWidget(self.slash,3,4,1,1,self.align)

        self.layout1.addWidget(self.quatre,4,1,1,1,self.align)
        self.layout1.addWidget(self.cinq,4,2,1,1,self.align)
        self.layout1.addWidget(self.six,4,3,1,1,self.align)
        self.layout1.addWidget(self.etoile,4,4,1,1,self.align)

        self.layout1.addWidget(self.un,5,1,1,1,self.align)
        self.layout1.addWidget(self.deux,5,2,1,1,self.align)
        self.layout1.addWidget(self.trois,5,3,1,1,self.align)
        self.layout1.addWidget(self.moins,5,4,1,1,self.align)

        self.layout1.addWidget(self.zero,6,1,1,1,self.align)
        self.layout1.addWidget(self.virgule,6,2,1,1,self.align)
        self.layout1.addWidget(self.egal,6,3,1,1,self.align)
        self.layout1.addWidget(self.plus,6,4,1,1,self.align)

        self.zero.clicked.connect(self.setVal0)
        self.un.clicked.connect(self.setVal1)
        self.deux.clicked.connect(self.setVal2)
        self.trois.clicked.connect(self.setVal3)
        self.quatre.clicked.connect(self.setVal4)
        self.cinq.clicked.connect(self.setVal5)
        self.six.clicked.connect(self.setVal6)
        self.sept.clicked.connect(self.setVal7)
        self.huit.clicked.connect(self.setVal8)
        self.neuf.clicked.connect(self.setVal9)
        self.plus.clicked.connect(self.setValPlus)
        self.moins.clicked.connect(self.setValMoins)
        self.slash.clicked.connect(self.setValSlash)
        self.etoile.clicked.connect(self.setValFois)
        self.virgule.clicked.connect(self.setValVirgule)
        self.C.clicked.connect(self.setVal0)

        self.setLayout(self.layout1)

    def setVal0(self) :
        buttonText = '0'
        self.line.setText(buttonText)

    def setVal1(self) :
        buttonText = '1'
        self.line.setText(buttonText)

    def setVal2(self) :
        buttonText = '2'
        self.line.setText(buttonText)

    def setVal3(self) :
        buttonText = '3'
        self.line.setText(buttonText)

    def setVal4(self) :
        buttonText = '4'
        self.line.setText(buttonText)

    def setVal5(self) :
        buttonText = '5'
        self.line.setText(buttonText)

    def setVal6(self) :
        buttonText = '6'
        self.line.setText(buttonText)

    def setVal7(self) :
        buttonText = '7'
        self.line.setText(buttonText)

    def setVal8(self) :
        buttonText = '8'
        self.line.setText(buttonText)

    def setVal9(self) :
        buttonText = '9'
        self.line.setText(buttonText)

    def setValMoins(self) :
        buttonText = '-'
        self.line.setText(buttonText)

    def setValPlus(self) :
        buttonText = '+'
        self.line.setText(buttonText)

    def setValFois(self) :
        buttonText = '*'
        self.line.setText(buttonText)

    def setValSlash(self) :
        buttonText = '/'
        self.line.setText(buttonText)

    def setValVirgule(self):
        buttonText = ','
        self.line.setText(buttonText)


if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()


