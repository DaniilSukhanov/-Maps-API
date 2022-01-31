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
        dolgota = float(self.lineEdit.text())
        shirote = float(self.lineEdit_3.text())
        mash = int(self.lineEdit_2.text())
        if mash in range(0, 18) and dolgota >= -180 and dolgota <= 180 and shirote >= -90 and\
                 shirote <= 90:
            self.get_map_image(f'{dolgota},{shirote}', str(mash))

    def get_map_image(self, ll, zoom, map_type='map'):
        params = {
            'll': ll,
            'z': zoom,
            'l': map_type
        }
        response = requests.get(self.PREFIX, params=params)
        if not response:
            print(
                f"""Ошибка!
                    Запрос: {self.PREFIX, params}
                    HTTP статус: {response.status_code}; {response.reason}"""
            )
        map_file = 'map_file.png'
        with open(map_file, "wb") as file:
            file.write(response.content)
        pixmap = QPixmap(map_file)
        print('somet')
        self.label.setPixmap(pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())