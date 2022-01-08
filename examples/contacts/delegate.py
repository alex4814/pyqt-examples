from typing import List, Any
from enum import Enum, auto
from PyQt5 import QtWidgets, QtGui, QtCore
from data import Contact
from style.palette import dark
from contactitem import ContactPlaceholder


class ContactDelegate(QtWidgets.QStyledItemDelegate):
    SizePlaceholderIcon = QtCore.QSize(48, 48)
    HeightPlaceholderIcon = SizePlaceholderIcon.height()
    SpacingPlaceholderIconText = 20
    HeightPlaceholderText = 24
    HeightPlaceholderGender = 40
    MarginLeftPlaceholderGenderLabel = 12
    BorderRadiusItem = 4
    BorderWidthItem = 2

    hoverItemChanged = QtCore.pyqtSignal(QtCore.QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap("./resource/add_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def sizeHint(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> QtCore.QSize:
        return QtCore.QSize(265, 348)

    def createEditor(self, parent: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex) -> QtWidgets.QWidget:
        contact: Contact = index.data(QtCore.Qt.UserRole)
        if True or contact.placeholder:
            w = ContactPlaceholder(parent)
            w.editingFinished.connect(self._commit_and_close_editor)
            print(f"creating editor for index {index.row()}: {w}")
            return w
        return super().createEditor(parent, option, index)

    @QtCore.pyqtSlot()
    def _commit_and_close_editor(self):
        editor = self.sender()
        # self.commitData.emit(editor)
        self.closeEditor.emit(editor)

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex):
        contact: Contact = index.data(QtCore.Qt.UserRole)

        if contact.placeholder:
            rect = option.rect.adjusted(0, 0, 0, -self.HeightPlaceholderGender)

            # background and border
            # REF: https://stackoverflow.com/a/29196812/3614952
            painter.save()
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            path = QtGui.QPainterPath()
            path.addRoundedRect(QtCore.QRectF(option.rect), self.BorderRadiusItem, self.BorderRadiusItem)
            pen = painter.pen()
            pen.setBrush(dark.midlight())
            pen.setWidth(self.BorderWidthItem)
            painter.setPen(pen)
            if option.state & QtWidgets.QStyle.State_MouseOver:
                painter.fillPath(path, dark.light())
            else:
                painter.fillPath(path, dark.dark())
            painter.drawPath(path)
            painter.restore()

            # r_icon = self._rect_placeholder_icon(option)
            pixmap = self._icon.pixmap(self.SizePlaceholderIcon)
            w_pixmap = pixmap.width() / pixmap.devicePixelRatio()
            h_pixmap = pixmap.height() / pixmap.devicePixelRatio()
            h_total = h_pixmap + self.SpacingPlaceholderIconText + self.HeightPlaceholderText
            x_pixmap = rect.x() + (rect.width() - w_pixmap) // 2
            y_pixmap = rect.y() + (rect.height() - h_total) // 2
            painter.drawPixmap(x_pixmap, y_pixmap, w_pixmap, h_pixmap, pixmap)

            # text
            painter.save()
            text_rect = QtCore.QRectF(rect.x(), y_pixmap, rect.width(), h_total)
            font = painter.font()
            font.setPixelSize(16)
            painter.setFont(font)
            pen = painter.pen()
            pen.setBrush(dark.buttonText())
            painter.setPen(pen)
            painter.drawText(text_rect, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, contact.name)
            painter.restore()

            # gender combo box

        else:
            # using qss to draw basic style
            # super().paint(painter, option, index)

            painter.save()
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            path = QtGui.QPainterPath()
            path.addRoundedRect(QtCore.QRectF(option.rect), self.BorderRadiusItem, self.BorderRadiusItem)
            pen = painter.pen()
            pen.setBrush(dark.midlight())
            pen.setWidth(self.BorderWidthItem)
            painter.setPen(pen)
            if option.state & QtWidgets.QStyle.State_MouseOver:
                painter.fillPath(path, dark.light())
            else:
                painter.fillPath(path, dark.dark())
            painter.drawPath(path)
            painter.restore()

    def _rect_placeholder_icon(self, option: QtWidgets.QStyleOptionViewItem):
        r = QtWidgets.QStyleOptionViewItem(option).rect
        height_hint = self.HeightPlaceholderIcon + self.HeightPlaceholderText + self.SpacingPlaceholderIconText
        r.setY((r.height() - self.HeightPlaceholderGender - height_hint) / 2)
        r.setHeight(self.HeightPlaceholderIcon)
        return r

    def _rect_placeholder_text(self, option: QtWidgets.QStyleOptionViewItem):
        r = QtWidgets.QStyleOptionViewItem(option).rect
        height_hint = self.HeightPlaceholderIcon + self.HeightPlaceholderText + self.SpacingPlaceholderIconText
        r.setY((r.height() - self.HeightPlaceholderGender - height_hint) / 2)
        r.setHeight(height_hint)
        return r

    def _rect_placeholder_gender(self, option: QtWidgets.QStyleOptionViewItem):
        r = QtWidgets.QStyleOptionViewItem(option).rect
        r.setY(r.height() - self.HeightPlaceholderGender)
        r.setHeight(self.HeightPlaceholderGender)
        return r
