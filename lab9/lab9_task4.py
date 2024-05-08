# Завдання 4

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import csv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 400)
        MainWindow.setStyleSheet("background-color: rgb(255, 221, 251);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(20, 150, 521, 201))
        self.label_image.setStyleSheet("background-color: white;")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.lineEdit_student = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_student.setGeometry(QtCore.QRect(20, 50, 211, 22))
        self.lineEdit_student.setStyleSheet("background-color:  rgb(170, 255, 209);")
        self.lineEdit_student.setObjectName("lineEdit_student")
        self.lineEdit_discipline = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_discipline.setGeometry(QtCore.QRect(270, 50, 161, 22))
        self.lineEdit_discipline.setStyleSheet("background-color: rgb(212, 255, 192);")
        self.lineEdit_discipline.setObjectName("lineEdit_discipline")
        self.spinBox_mark = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_mark.setGeometry(QtCore.QRect(470, 50, 71, 22))
        self.spinBox_mark.setStyleSheet("background-color: rgb(248, 247, 205);")
        self.spinBox_mark.setObjectName("spinBox_mark")
        self.label_student = QtWidgets.QLabel(self.centralwidget)
        self.label_student.setGeometry(QtCore.QRect(100, 20, 51, 16))
        self.label_student.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_student.setTextFormat(QtCore.Qt.PlainText)
        self.label_student.setObjectName("label_student")
        self.label_discipline = QtWidgets.QLabel(self.centralwidget)
        self.label_discipline.setGeometry(QtCore.QRect(320, 20, 71, 16))
        self.label_discipline.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_discipline.setTextFormat(QtCore.Qt.PlainText)
        self.label_discipline.setObjectName("label_discipline")
        self.label_mark = QtWidgets.QLabel(self.centralwidget)
        self.label_mark.setGeometry(QtCore.QRect(490, 20, 41, 16))
        self.label_mark.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_mark.setTextFormat(QtCore.Qt.PlainText)
        self.label_mark.setObjectName("label_mark")
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(240, 110, 93, 28))
        self.pushButton_save.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(255, 174, 108);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(20, 110, 151, 28))
        self.pushButton_load.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
                                           "background-color: rgb(173, 255, 251);")
        self.pushButton_load.setObjectName("pushButton_load")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 26))
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.action_1 = QtWidgets.QAction(MainWindow)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_1)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        # комбо радіо і прогресс бар
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(580, 50, 150, 22))
        self.comboBox.setObjectName("comboBox")

        self.radioButton_student = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_student.setGeometry(QtCore.QRect(580, 80, 82, 17))
        self.radioButton_student.setObjectName("radioButton_student")
        self.radioButton_student.setChecked(True)

        self.radioButton_discipline = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_discipline.setGeometry(QtCore.QRect(580, 110, 82, 17))
        self.radioButton_discipline.setObjectName("radioButton_discipline")

        self.radioButton_mark = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_mark.setGeometry(QtCore.QRect(580, 150, 82, 17))
        self.radioButton_mark.setObjectName("radioButton_mark")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(580, 190, 118, 23))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(5)
        self.progressBar.setValue(0)
        self.progressBar.hide()
        self.radioButton_mark.toggled.connect(self.t_prog_bar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_student.setText(_translate("MainWindow", "Студент"))
        self.label_discipline.setText(_translate("MainWindow", "Дисципліна"))
        self.label_mark.setText(_translate("MainWindow", "Оцінка"))
        self.pushButton_save.setText(_translate("MainWindow", "Зберегти"))
        self.pushButton_load.setText(_translate("MainWindow", "Завантажити зображення"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_1.setText(_translate("MainWindow", "Пункт 1"))
        self.action_2.setText(_translate("MainWindow", "Пункт 2"))
        self.action_3.setText(_translate("MainWindow", "Пункт 3"))
        self.radioButton_student.setText(_translate("MainWindow", "Студент"))
        self.radioButton_discipline.setText(_translate("MainWindow", "Дисципліна"))
        self.radioButton_mark.setText(_translate("MainWindow", "Оцінка"))
        self.pushButton_save.clicked.connect(self.save_data)
        self.pushButton_load.clicked.connect(self.load_image)

    def save_data(self):
        student = self.lineEdit_student.text()
        discipline = self.lineEdit_discipline.text()
        mark = self.spinBox_mark.value()

        with open('l9_t2_students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student, discipline, mark])

        self.lineEdit_student.clear()
        self.lineEdit_discipline.clear()
        self.spinBox_mark.setValue(0)

        self.comboBox.clear()
        if self.radioButton_student.isChecked():
            self.comboBox.addItem(student)
        elif self.radioButton_discipline.isChecked():
            self.comboBox.addItem(discipline)
        elif self.radioButton_mark.isChecked():
            self.comboBox.addItem(str(mark))
        self.update_bar()

    def load_image(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Виберіть зображення', '',
                                                             'Images (*.png *.jpg)', options=options)
        if file_name:
            pixmap = QtGui.QPixmap(file_name)
            self.label_image.setPixmap(pixmap)

    def t_prog_bar(self, checked):
        if checked:
            self.progressBar.show()
        else:
            self.progressBar.hide()
        self.update_bar()

    def update_bar(self):
        if self.radioButton_mark.isChecked():
            with open('l9_t2_students.csv', 'r', newline="") as file:
                reader = csv.reader(file)
                last_row = None
                for row in reader:
                    if row:
                        last_row = row
                if last_row:
                    last_mark = int(last_row[2])
                    self.progressBar.setValue(last_mark)
        else:
            self.progressBar.setValue(0)  # reset бару


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
