import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from datetime import datetime

colors = ['#053061', '#2166ac', '#4393c3', '#92c5de', 'dle5f0', '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d',
          '#b2182b', '#67001f']


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-$d")
            return value

            # if isinstance(value, float):
            #     return "%.2f" % value
            # if isinstance(value, str):
            #     return '"%s"' % value
            # return value

            # return self._data[index.row()][index.column()]

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            # if isinstance(value, datetime):
            #     return QtGui.QIcon('calendar.png')
            # if isinstance(value, bool):
            #     if value:
            #         return QtGui.QIcon('tick.png')
            #     return QtGui.QIcon('cross.png')
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)
                value = max(-5, value)
                value = min(5, value)
                value = value + 5
            return QtGui.QColor(colors[value])

        if role == Qt.BackgroundRole and index.column() == 2:
            return QtGui.QColor('red')

        if role == Qt.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                return Qt.AlignVCenter + Qt.AlignRight

        if role == Qt.ForegroundRole:
            value = self._data[index.row()][index.column()]
        if (isinstance(value, int) or isinstance(value, float)) and value < 0:
            return QtGui.QColor('red')

        if role == Qt.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)
                value = max(-5, value)
                value = min(5, value)
                value = value + 5
                return QtGui.QColor(colors[value])

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QtWidgets.QTableView()

        data = [
            [4, 9, 2],
            [1, -1, 'hello'],
            [3.023, 5, -5],
            [3, 3, datetime],
            [7.555, 8, 9],
        ]

        # data = [
        #     [4, 9, 2],
        #     [1, 0, 0],
        #     [3, 5, 0],
        #     [3, 3, 2],
        #     [7, 8, 9],
        # ]

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

# table = [
#     [4, 9, 2],
#     [1, 1, 1],
#     [3, 5, 5],
#     [3, 3, 2],
#     [7, 8, 9],
# ]
#
# row = 4
# col = 2
# print(table[col])
# print(table[col][row])
