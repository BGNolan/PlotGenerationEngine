from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import mainwindow
import statebrowser

import os

class StateBrowserWindow(QtWidgets.QMainWindow, statebrowser.Ui_StateBrowser):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.listWidget.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PlotGenerationEngine()
    window.show()
    sys.exit(app.exec_())
