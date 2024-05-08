# Завдання 6

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMdiArea, QMdiSubWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Завдання 6')
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu('Меню')
        new_action = QAction('Нове вікно', self)
        new_action.triggered.connect(self.new_window)
        file.addAction(new_action)

        cascad_action = QAction('Каскадний спосіб', self)
        cascad_action.triggered.connect(self.mdi.cascadeSubWindows)
        file.addAction(cascad_action)

        tile_action = QAction('Плитковий спосіб', self)
        tile_action.triggered.connect(self.mdi.tileSubWindows)
        file.addAction(tile_action)
        self.opened_windows = 0

    def new_window(self):
        if self.opened_windows < 2:
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            self.mdi.addSubWindow(sub)
            sub.show()
            self.opened_windows += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
