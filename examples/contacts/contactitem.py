from PyQt5 import QtWidgets, QtGui, QtCore
from placeholderitem import Ui_Form


class ContactPlaceholder(QtWidgets.QWidget):
    editingFinished = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
        self.setAutoFillBackground(True)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.editingFinished.emit()
        super().leaveEvent(a0)
        print(f"editor {self} leave event processed")
