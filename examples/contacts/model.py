from typing import List, Any
from PyQt5 import QtWidgets, QtGui, QtCore
from data import Contact


class ContactModel(QtCore.QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._contacts = []

    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        return QtCore.Qt.ItemFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)

    def populate(self, contacts: List[Contact]):
        self.beginResetModel()
        self._contacts = [Contact("Add Contact", 0, "", True)] + contacts
        self.endResetModel()

    def rowCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()) -> int:
        return 0 if parent.isValid() else len(self._contacts)

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole) -> Any:
        if not index.isValid():
            return
        if role == QtCore.Qt.UserRole:
            contact = self._contacts[index.row()]
            return contact
