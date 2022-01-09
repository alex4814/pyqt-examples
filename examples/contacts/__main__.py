import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from mainwindow import Ui_MainWindow
from model import ContactModel
from delegate import ContactDelegate
from data import contacts


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        # self.init_conn()

    def init_ui(self):
        self.ui.contactsView.setViewMode(QtWidgets.QListView.IconMode)
        self.ui.contactsView.setResizeMode(QtWidgets.QListView.Adjust)
        self.ui.contactsView.setSpacing(20)
        self.ui.contactsView.setGridSize(QtCore.QSize(275, 348))
        self.ui.contactsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ui.contactsView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.ui.contactsView.setMouseTracking(True)

        model = ContactModel()
        model.populate(contacts)
        self.ui.contactsView.setModel(model)
        delegate = ContactDelegate(self.ui.contactsView)
        self.ui.contactsView.setItemDelegate(delegate)

    def init_conn(self):
        self.ui.contactsView.entered.connect(self.ui.contactsView.edit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    with open("./style/dark.qss") as fp:
        app.setStyleSheet(fp.read())

    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())
