import sys

from dis import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QKeyEvent, QWheelEvent
from PyQt5.QtCore import Qt

from request import get_map_image


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load_image.clicked.connect(self.read_input)
        # Вызов функции при обновлении значения
        self.doubleSpinBox_latitude.valueChanged.connect(self.read_input)
        self.doubleSpinBox_longitude.valueChanged.connect(self.read_input)
        self.spinBox_zoom.valueChanged.connect(self.set_step_spinbox)
        self.comboBox_layer.currentTextChanged.connect(self.read_input)
        self.set_step_spinbox()
        self.keys = {
            Qt.Key_Up: self.doubleSpinBox_longitude.stepUp,
            Qt.Key_Down: self.doubleSpinBox_longitude.stepDown,
            Qt.Key_Left: self.doubleSpinBox_latitude.stepDown,
            Qt.Key_Right: self.doubleSpinBox_latitude.stepUp
        }

    def set_step_spinbox(self):
        """Ставит размер шагов для spinbox широты и долготы"""
        k = 2 ** self.spinBox_zoom.value()
        spn_longitude = 90 / k
        spn_latitude = 180 / k
        self.doubleSpinBox_longitude.setSingleStep(spn_longitude)
        self.doubleSpinBox_latitude.setSingleStep(spn_latitude)
        self.read_input()

    def wheelEvent(self, event: QWheelEvent):
        """Управлением масштабом (колесо мыши)"""
        if event.angleDelta().y() < 0:
            self.spinBox_zoom.stepDown()
        else:
            self.spinBox_zoom.stepUp()

    def keyPressEvent(self, event: QKeyEvent):
        """Управление координатами (перемещение стрелками)"""
        result = self.keys.get(event.key(), None)
        if result is not None:
            result()

    def read_input(self):
        """Прочтение вводимых данных"""
        latitude = self.doubleSpinBox_latitude.value()
        longitude = self.doubleSpinBox_longitude.value()
        self.label_image.setPixmap(
            get_map_image(
                f'{latitude},{longitude}',
                f'{self.doubleSpinBox_latitude.singleStep()},'
                f'{self.doubleSpinBox_longitude.singleStep()}',
                self.comboBox_layer.currentText()
            )
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
