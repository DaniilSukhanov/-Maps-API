import sys

from dis import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

from request import get_map_image


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load_image.clicked.connect(self.read_input)

    def wheelEvent(self, event):
        """Управлением масштабом (колесо мыши)"""
        if event.angleDelta().y() < 0:
            self.spinBox_zoom.stepDown()
        else:
            self.spinBox_zoom.stepUp()
        self.read_input()

    def read_input(self):
        dolgota = self.doubleSpinBox_latitude.value()
        shirote = self.doubleSpinBox_longitude.value()
        zoom = self.spinBox_zoom.value()
        self.label_image.setPixmap(
            get_map_image(f'{dolgota},{shirote}', zoom)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
