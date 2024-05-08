# Лабораторна робота №9
# Завдання 1

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
import random


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Завдання 1')
        self.setGeometry(100, 100, 300, 150)
        self.layout = QVBoxLayout()
        self.label = QLabel('Маслова Віталія')
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Змінити колір')
        self.button.clicked.connect(self.ChangeColor)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def ChangeColor(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.label.setStyleSheet('color: ' + color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
