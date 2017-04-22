from PyQt5 import QtWidgets, QtCore, QtGui

from view import dragButton

class DragWidget(QtWidgets.QScrollArea):
    item = None
    def getDraggedItem(self):

        self.item

    def setDraggedItem(self, item):
        print("setting the dragged item" + str(item.pos()))
        self.item = item

    def __init__(self, parent=None):
        super(DragWidget, self).__init__(parent)
        item = dragButton.DragButton("")

        self.initUI()

    def initUI(self):

        self.setAcceptDrops(True)

#        self.button = Button('Button', self)
#        self.button.move(100, 65)

#        self.setWindowTitle('Click or Move')
#        self.setGeometry(300, 300, 280, 150)
        self.show()

    def dragEnterEvent(self, e):
        #self.setDraggedItem( self.childAt(e.pos()) )
        e.accept()

    def dropEvent(self, e):

        posB = e.pos()
        print("posA ->" + str(self.item.pos()) + ", posB ->" + str(posB))
        self.item.move(posB.x() - (self.item.width()/2), posB.y() - (self.item.height()/2))

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
