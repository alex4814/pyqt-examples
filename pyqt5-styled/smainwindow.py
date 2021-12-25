import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from smainwindow_ui import Ui_SMainWindow


class SMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(SMainWindow, self).__init__(parent)
        self.ui = Ui_SMainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    @QtCore.pyqtSlot()
    def toggle_maximized(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wnd = SMainWindow()
    wnd.show()
    sys.exit(app.exec())
