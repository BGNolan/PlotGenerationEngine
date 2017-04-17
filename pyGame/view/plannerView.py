from PyQt5 import QtCore, QtGui, QtWidgets

class PlannerView(QtWidgets.QGraphicsView):
    def __init__(self, scene, parent=None):
        QtWidgets.QGraphicsView.__init__(self, scene, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        #if e.mimeData().hasFormat('text/plain'):
        e.accept()
        #else:
        #    e.ignore()

    def dropEvent(self, e):
        self.setText("I dragged a thing and then dropped it")
