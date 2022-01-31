import sys

from ui_file import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from request import get_map_image

SCREEN_SIZE = [1000, 600]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.read_input)

    def read_input(self):
        dolgota = float(self.lineEdit.text())
        shirote = float(self.lineEdit_3.text())
        mash = int(self.lineEdit_2.text())
        try:
            self.label.setPixmap(get_map_image(f'{dolgota},{shirote}', mash))
        except AssertionError:
            self.label.setText('Некорректные данные!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())