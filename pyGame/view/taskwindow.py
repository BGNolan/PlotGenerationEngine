from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import preconditions_v2 as pc

import mainwindow
import dialog

import os

class TaskWindow(QtWidgets.QMainWindow, dialog.Ui_Dialog):
    @property
    def task(self):
        return self._task
    @task.setter
    def task(self, value):
        self._task = value
        self.listWidget.clear()
        self.label.setText(value)
        self.listWidget_2.addItem("- Preconditions:")
        for precondition in pc.preconditionsForTasks[value]:
            self.listWidget_2.addItem(precondition)


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self._task = None
        self.listWidget.addItem("No Task")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TaskWindow()
    window.show()
    sys.exit(app.exec_())
