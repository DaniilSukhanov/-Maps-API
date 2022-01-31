import sys

import requests
from PyQt5.QtGui import QPixmap
from ui_file import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

SCREEN_SIZE = [1000, 600]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.read_input)
        self.PREFIX = 'https://static-maps.yandex.ru/1.x/?'
        self.APIKEY = "40d1649f-0493-4b70-98ba-98533de7710b"

    def read_input(self):
        dolgota = self.lineEdit.text()
        shirote = self.lineEdit_3.text()
        mash = self.lineEdit_2.text()
        print(3)
        # if mash in range(0, 18) and float(dolgota) >= -180 and float(dolgota) <= 180 and float(shirote) >= -90 and\
        #         float(shirote) <= 90:
        self.get_map_image(f'{float(dolgota)},{float(shirote)}', int(mash))

    def get_map_image(self, ll, zoom, map_type='map'):
        print(1)
        params = {
            'll': ll,
            'z': zoom,
            'l': map_type,
            'key': self.APIKEY
        }
        response = requests.get(self.PREFIX, params=params)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        self.label.setPixmap(pixmap)
        print('something')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())