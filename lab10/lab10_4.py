# MATPLOTLIB ТА QT
import random
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)
        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]

        self._plot_ref = None  # перемалювати на місці

        self.update_plot()
        self.show()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]

        if self._plot_ref is None:  # перемалювати на місці
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'r')
            self._plot_ref = plot_refs[0]
        else:
            self._plot_ref.set_ydata(self.ydata)
        self.canvas.draw()

        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas.draw()

        # toolbar = NavigationToolbar(sc, self)
        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(toolbar)
        # layout.addWidget(sc)
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)
        #
        # # self.setCentralWidget(sc)
        # self.setCentralWidget(widget)
        # self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
