# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statebrowser.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StateBrowser(object):
    def setupUi(self, StateBrowser):
        StateBrowser.setObjectName("StateBrowser")
        StateBrowser.resize(721, 469)
        self.leftCol = QtWidgets.QWidget(StateBrowser)
        self.leftCol.setGeometry(QtCore.QRect(-1, 29, 361, 441))
        self.leftCol.setObjectName("leftCol")
        self.listWidget = QtWidgets.QListWidget(self.leftCol)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 351, 461))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.rightCol = QtWidgets.QWidget(StateBrowser)
        self.rightCol.setGeometry(QtCore.QRect(360, 30, 361, 441))
        self.rightCol.setObjectName("rightCol")
        self.listWidget_2 = QtWidgets.QListWidget(self.rightCol)
        self.listWidget_2.setGeometry(QtCore.QRect(5, 1, 341, 491))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(StateBrowser)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(StateBrowser)
        self.label_3.setGeometry(QtCore.QRect(90, 10, 71, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(StateBrowser)
        QtCore.QMetaObject.connectSlotsByName(StateBrowser)

    def retranslateUi(self, StateBrowser):
        _translate = QtCore.QCoreApplication.translate
        StateBrowser.setWindowTitle(_translate("StateBrowser", "State Browser"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("StateBrowser", "Blocks: A, B, C"))
        item = self.listWidget.item(1)
        item.setText(_translate("StateBrowser", "Pyramids: 1, 2, 3"))
        item = self.listWidget.item(2)
        item.setText(_translate("StateBrowser", "Positions: A, B, C, inHand"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("StateBrowser", "Initial State"))
        self.label_3.setText(_translate("StateBrowser", "-> Task A"))
