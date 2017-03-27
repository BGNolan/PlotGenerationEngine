from PyQt5 import QtCore, QtWidgets
import sys

import blocks_world_operators
from pyhop_module.blocks_world_methods import *
from pyhop_module.blocks_world_methods2 import *
from pyhop_module.pyhop import *

import os

import view.mainwindow as mainwindow
import view.statebrowserwindow as statebrowserwindow
import view.taskwindow as taskwindow
from pyhop_module.pyhop import *


class PlotGenerationEngine(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(PlotGenerationEngine, self).__init__(parent)
        self.setupUi(self)

        self.stateBrowserWindow = None
        self.taskWindow = None
        self.actionOpen.triggered.connect(self.browseFolder)
        self.actionState_Browser.triggered.connect(self.showStateBrowser)
        self.actionPlanner.triggered.connect(self.hideStateBrowser)
        self.pushButton_2.clicked.connect(self.showStateBrowser)
        self.pushButton_3.clicked.connect(self.showStateBrowser)
        self.pushButton.clicked.connect( lambda: self.showTaskWindow('pickup') )
        self.populateTasks()

    def browseFolder(self):
        #self.listWidget.clear()
        file_name = str(QtWidgets.QFileDialog.getOpenFileName(self)[0])

        currentp = QtCore.QDir.current()
        relativeName = currentp.relativeFilePath(file_name)
        self.setWindowTitle(relativeName)

    def showStateBrowser(self):
        if self.stateBrowserWindow is None:
            self.stateBrowserWindow = statebrowserwindow.StateBrowserWindow(self)
        self.stateBrowserWindow.show()

    def hideStateBrowser(self):
        if self.stateBrowserWindow is not None:
            self.stateBrowserWindow.hide()

    def showTaskWindow(self, task):
        if self.taskWindow is None:
            self.taskWindow = taskwindow.TaskWindow(self)

        self.taskWindow.task = task
        self.taskWindow.show()

    def populateTasks(self):
        tasks = get_operators()
        layout = QtWidgets.QGridLayout(self.tasksList)
        row = 0
        col = 0
        for taskName in tasks:
                layout.addWidget(QtWidgets.QPushButton(taskName),row,col)
                if col < 2:
                    col += 1
                else:
                    col = 0
                    row += 1
        self.scrollAreaWidgetContents.setLayout(layout)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = PlotGenerationEngine()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
