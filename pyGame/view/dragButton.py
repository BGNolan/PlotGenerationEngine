from PyQt5 import QtWidgets, QtCore, QtGui

class DragButton(QtWidgets.QPushButton):

    def __init__(self, title):
        super(DragButton, self).__init__(title)
        #self.move(200,100)

    def mouseMoveEvent(self, e):

        if e.buttons() != QtCore.Qt.LeftButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.parent().setDraggedItem(self)
        dropAction = drag.exec(QtCore.Qt.MoveAction)

    def mousePressEvent(self, e):

        super(DragButton, self).mousePressEvent(e)

        #if e.button() == QtCore.Qt.LeftButton:
            #print('press')
