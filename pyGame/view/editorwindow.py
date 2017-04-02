from PyQt5 import QtGui, QtCore, QtWidgets
import sys

from view import mainwindow, editor

import os

class EditorWindow(QtWidgets.QMainWindow, editor.Ui_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = EditorWindow()
    window.show()
    sys.exit(app.exec_())
