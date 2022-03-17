# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 547)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_layer = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_layer.setEnabled(True)
        self.comboBox_layer.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox_layer.setAutoFillBackground(False)
        self.comboBox_layer.setEditable(False)
        self.comboBox_layer.setDuplicatesEnabled(False)
        self.comboBox_layer.setFrame(True)
        self.comboBox_layer.setObjectName("comboBox_layer")
        self.comboBox_layer.addItem("")
        self.comboBox_layer.addItem("")
        self.comboBox_layer.addItem("")
        self.gridLayout.addWidget(self.comboBox_layer, 0, 7, 1, 1)
        self.doubleSpinBox_longitude = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_longitude.setMouseTracking(False)
        self.doubleSpinBox_longitude.setTabletTracking(False)
        self.doubleSpinBox_longitude.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.doubleSpinBox_longitude.setAcceptDrops(False)
        self.doubleSpinBox_longitude.setWrapping(False)
        self.doubleSpinBox_longitude.setFrame(True)
        self.doubleSpinBox_longitude.setReadOnly(False)
        self.doubleSpinBox_longitude.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_longitude.setKeyboardTracking(True)
        self.doubleSpinBox_longitude.setDecimals(5)
        self.doubleSpinBox_longitude.setMinimum(-90.0)
        self.doubleSpinBox_longitude.setMaximum(90.0)
        self.doubleSpinBox_longitude.setSingleStep(0.0)
        self.doubleSpinBox_longitude.setProperty("value", 0.0)
        self.doubleSpinBox_longitude.setObjectName("doubleSpinBox_longitude")
        self.gridLayout.addWidget(self.doubleSpinBox_longitude, 0, 3, 1, 1)
        self.lineEdit_search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout.addWidget(self.lineEdit_search, 2, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 4, 0, 1, 8)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 2, 5, 1, 1)
        self.pushButton_clear_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear_search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_clear_search.setObjectName("pushButton_clear_search")
        self.gridLayout.addWidget(self.pushButton_clear_search, 2, 6, 1, 2)
        self.spinBox_zoom = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_zoom.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spinBox_zoom.setAcceptDrops(False)
        self.spinBox_zoom.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.spinBox_zoom.setMaximum(17)
        self.spinBox_zoom.setSingleStep(1)
        self.spinBox_zoom.setObjectName("spinBox_zoom")
        self.gridLayout.addWidget(self.spinBox_zoom, 0, 5, 1, 1)
        self.doubleSpinBox_latitude = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_latitude.setEnabled(True)
        self.doubleSpinBox_latitude.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.doubleSpinBox_latitude.setAcceptDrops(False)
        self.doubleSpinBox_latitude.setAutoFillBackground(False)
        self.doubleSpinBox_latitude.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox_latitude.setKeyboardTracking(True)
        self.doubleSpinBox_latitude.setProperty("showGroupSeparator", False)
        self.doubleSpinBox_latitude.setDecimals(5)
        self.doubleSpinBox_latitude.setMinimum(-180.0)
        self.doubleSpinBox_latitude.setMaximum(180.0)
        self.doubleSpinBox_latitude.setSingleStep(0.0)
        self.doubleSpinBox_latitude.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_latitude.setObjectName("doubleSpinBox_latitude")
        self.gridLayout.addWidget(self.doubleSpinBox_latitude, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
        self.checkBox_switch_postcode = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_switch_postcode.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.checkBox_switch_postcode.setTristate(False)
        self.checkBox_switch_postcode.setObjectName("checkBox_switch_postcode")
        self.gridLayout.addWidget(self.checkBox_switch_postcode, 5, 0, 1, 2)
        self.label_address = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_address.sizePolicy().hasHeightForWidth())
        self.label_address.setSizePolicy(sizePolicy)
        self.label_address.setTextFormat(QtCore.Qt.AutoText)
        self.label_address.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_address.setObjectName("label_address")
        self.gridLayout.addWidget(self.label_address, 5, 2, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_layer.setItemText(0, _translate("MainWindow", "map"))
        self.comboBox_layer.setItemText(1, _translate("MainWindow", "sat"))
        self.comboBox_layer.setItemText(2, _translate("MainWindow", "sat,skl"))
        self.label_2.setText(_translate("MainWindow", "Широта"))
        self.label_image.setText(_translate("MainWindow", "Image"))
        self.label_4.setText(_translate("MainWindow", "Слой"))
        self.label.setText(_translate("MainWindow", "Долгота"))
        self.pushButton_search.setText(_translate("MainWindow", "Искать"))
        self.pushButton_clear_search.setText(_translate("MainWindow", "Сброс поискового результата"))
        self.label_3.setText(_translate("MainWindow", "Маштаб"))
        self.checkBox_switch_postcode.setText(_translate("MainWindow", "Почтовый индекс"))
        self.label_address.setText(_translate("MainWindow", "Адрес не найден"))
