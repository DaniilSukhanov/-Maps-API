import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

SCREEN_SIZE = [1000, 600]



class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('dis.ui', self)
        self.getImage()
        self.pushButton.clicked.connect(self.read_input)

    def read_input(self):
        dolgota = self.lineEdit.text()
        shirote = self.lineEdit_3.text()
        mash = self.lineEdit_2.text()
        if mash in range(0, 18) and float(dolgota) >= -180 and float(dolgota) <= 180 and float(shirote) >= -90 and\
                float(shirote) <= 90:
            pass #передача параметров в карту


    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())