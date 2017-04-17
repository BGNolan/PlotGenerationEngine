from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import blocks_world_operators
from pyhop_module.blocks_world_methods import *
from pyhop_module.blocks_world_methods2 import *
from preconditions_module.t7_pyhop_v1 import *
from model.plan_tree import *

from view import mainwindow, statebrowserwindow, taskwindow, editorwindow, plannerView, dragButton

import os

class PlotGenerationEngine(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    openedFile = None
    currentp = QtCore.QDir.current()
    def __init__(self, parent=None):
        super(PlotGenerationEngine, self).__init__(parent)
        self.setupUi(self)

        self.stateBrowserWindow = None
        self.taskWindow = None
        self.editorWindow = None

        #ellipse = QtWidgets.QGraphicsEllipseItem(20,20,100,200)
        pen = QtGui.QPen(QtGui.QColor("black"))
        brush = QtGui.QBrush(QtGui.QColor(100,100,255,100))
        rect = QtWidgets.QGraphicsRectItem(20,20,80,30)
        rect.setBrush(brush)
        rect.setPen(pen)


        self.scene=QtWidgets.QGraphicsScene(self)
        #self.scene.addText("Hello, world!")
        self.scene.addItem(rect)
        rect.setFlags(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.view = plannerView.PlannerView(self.scene, self.leftCol)
        self.view.setMinimumSize(510,490)
        self.leftCol.show()

        self.actionOpen.triggered.connect(self.browseFolder)
        self.actionState_Browser.triggered.connect(self.showStateBrowser)
        self.actionPlanner.triggered.connect(self.hideStateBrowser)
        self.actionEditor.triggered.connect(self.showEditor)
#        self.pushButton_2.clicked.connect(self.showStateBrowser)
#        self.pushButton_3.clicked.connect(self.showStateBrowser)
#        self.pushButton.clicked.connect( lambda: self.showTaskWindow('pickup') )
        self.populateTasks()

    def browseFolder(self):
        #self.listWidget.clear()
        file_name = str(QtWidgets.QFileDialog.getOpenFileName(self)[0])
        self.openedFile = file_name
        relativeName = self.currentp.relativeFilePath(self.openedFile)
        self.setWindowTitle(relativeName)

    def showEditor(self):
        if self.editorWindow is None:
            self.editorWindow = editorwindow.EditorWindow(self)
        self.editorWindow.show()


    def showStateBrowser(self):
        if self.stateBrowserWindow is None:
            self.stateBrowserWindow = statebrowserwindow.StateBrowserWindow(self)
            if self.openedFile is not None:
                self.stateBrowserWindow.listWidget.clear()
                self.stateBrowserWindow.listWidget.addItem(self.currentp.relativeFilePath(self.openedFile))
            else:
                self.stateBrowserWindow.listWidget.clear()
                self.stateBrowserWindow.listWidget.addItem("No opened file")
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
                layout.addWidget(dragButton.DragButton(taskName),row,col)
                if col < 2:
                    col += 1
                else:
                    col = 0
                    row += 1
        self.tasksList.setLayout(layout)


def main():
    app = QtWidgets.QApplication(sys.argv)
    # [('unstack', 'a', 'b'), ('putdown', 'a'), ('pickup', 'b'), ('stack', 'b', 'a'), ('pickup', 'c'), ('stack', 'c', 'b')]
    #['unstack', 'pickup', 'putdown', 'stack']
    #Plan

    test_tree = Plan_Tree()
    test_tree.add_task(('unstack', 'a', 'b'))
    test_tree.add_task(('putdown', 'a'),test_tree.root)
    test_tree.add_task(('pickup', 'b'),test_tree.root)
    test_tree.add_task(('stack', 'b', 'a'),test_tree.nodes[2])
    test_tree.display_all()

    node = test_tree.get_node(4)
    plan = test_tree.get_plan(node)
    for task in plan:
        print('Task: '+ ', '.join(task))


    form = PlotGenerationEngine()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
