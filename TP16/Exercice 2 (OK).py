from PySide2.QtWidgets import *
from PySide2.QtGui import *


class Win(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.setWindowTitle('IHM')
        self.setFixedSize(200,200)
        self.progressbar = QProgressBar()
        self.slider = QSlider()

        self.layout.addWidget(self.progressbar)
        self.layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.progress)
        #val = self.slider.value()
        self.setLayout(self.layout)

    def progress(self):
        val = self.slider.value()
        self.progressbar.setValue(val)


if __name__ == '__main__':
    app = QApplication([])
    window = Win()
    window.show()
    app.exec_()
