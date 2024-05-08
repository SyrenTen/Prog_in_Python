# Завдання 5

import sys
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 216)
        MainWindow.setStyleSheet("background-color: rgb(255, 221, 251);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 50, 150, 50))
        self.pushButton_1.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 174, 108);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 120, 150, 50))
        self.pushButton_2.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 174, 108);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 50, 150, 50))
        self.pushButton_3.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 174, 108);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 120, 150, 50))
        self.pushButton_4.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 174, 108);")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_1.clicked.connect(lambda: self.show_message_box('Увага! Повідомлення 1!'))
        self.pushButton_2.clicked.connect(lambda: self.show_message_box('Сбогодні буде дощ'))
        self.pushButton_3.clicked.connect(lambda: self.show_message_box('Повідомлення 3!'))
        self.pushButton_4.clicked.connect(lambda: self.show_message_box('Відбудеться землетрус'))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_1.setText(_translate("MainWindow", "Кнопка 1"))
        self.pushButton_2.setText(_translate("MainWindow", 'Кнопка 2'))
        self.pushButton_3.setText(_translate("MainWindow", 'Кнопка 3'))
        self.pushButton_4.setText(_translate("MainWindow", 'Кнопка 4'))

    def show_message_box(self, message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Інформаційне повідомлення')
        msg_box.setText(message)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
