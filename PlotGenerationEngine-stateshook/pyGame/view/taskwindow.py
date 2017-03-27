from PyQt5 import QtGui, QtCore, QtWidgets
import sys

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
        self.label.setText(value["Task"]["Name"])
        self.listWidget.addItem("- Parameters:")
        self.listWidget_2.addItem("- Preconditions:")
        for key in value["Task"]["Parameters"]:
            self.listWidget.addItem(key + ": " + value["Task"]["Parameters"][key])
        for key in value["Task"]["Preconditions"]:
            self.listWidget_2.addItem(key + ": " + value["Task"]["Preconditions"][key])


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
