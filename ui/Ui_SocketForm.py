# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/socket_form.ui'
#
# Created: Wed Oct 14 11:22:00 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SocketForm(object):
    def setupUi(self, SocketForm):
        SocketForm.setObjectName(_fromUtf8("SocketForm"))
        SocketForm.resize(739, 549)
        self.gridLayout = QtGui.QGridLayout(SocketForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(SocketForm)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.recvTextBrowser = QtGui.QTextBrowser(self.splitter)
        self.recvTextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.recvTextBrowser.setObjectName(_fromUtf8("recvTextBrowser"))
        self.sendPlainTextEdit = QtGui.QPlainTextEdit(self.splitter)
        self.sendPlainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.sendPlainTextEdit.setObjectName(_fromUtf8("sendPlainTextEdit"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(SocketForm)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.rxLcdNumber = QtGui.QLCDNumber(SocketForm)
        self.rxLcdNumber.setObjectName(_fromUtf8("rxLcdNumber"))
        self.horizontalLayout.addWidget(self.rxLcdNumber)
        self.label_2 = QtGui.QLabel(SocketForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.txLcdNumber = QtGui.QLCDNumber(SocketForm)
        self.txLcdNumber.setObjectName(_fromUtf8("txLcdNumber"))
        self.horizontalLayout.addWidget(self.txLcdNumber)
        self.resetBytesBtn = QtGui.QPushButton(SocketForm)
        self.resetBytesBtn.setObjectName(_fromUtf8("resetBytesBtn"))
        self.horizontalLayout.addWidget(self.resetBytesBtn)
        self.label_3 = QtGui.QLabel(SocketForm)
        self.label_3.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.repeatTimesCbx = QtGui.QComboBox(SocketForm)
        self.repeatTimesCbx.setMaximumSize(QtCore.QSize(102, 16777215))
        self.repeatTimesCbx.setEditable(True)
        self.repeatTimesCbx.setObjectName(_fromUtf8("repeatTimesCbx"))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.repeatTimesCbx)
        self.hexModeCkb = QtGui.QCheckBox(SocketForm)
        self.hexModeCkb.setObjectName(_fromUtf8("hexModeCkb"))
        self.horizontalLayout.addWidget(self.hexModeCkb)
        spacerItem = QtGui.QSpacerItem(608, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cleanBtn = QtGui.QPushButton(SocketForm)
        self.cleanBtn.setObjectName(_fromUtf8("cleanBtn"))
        self.horizontalLayout.addWidget(self.cleanBtn)
        self.sendBtn = QtGui.QPushButton(SocketForm)
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.horizontalLayout.addWidget(self.sendBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(SocketForm)
        QtCore.QMetaObject.connectSlotsByName(SocketForm)

    def retranslateUi(self, SocketForm):
        SocketForm.setWindowTitle(QtGui.QApplication.translate("SocketForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SocketForm", "Rx", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SocketForm", "Tx", None, QtGui.QApplication.UnicodeUTF8))
        self.resetBytesBtn.setText(QtGui.QApplication.translate("SocketForm", "清零", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SocketForm", "重复发送", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(0, QtGui.QApplication.translate("SocketForm", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(1, QtGui.QApplication.translate("SocketForm", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(2, QtGui.QApplication.translate("SocketForm", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(3, QtGui.QApplication.translate("SocketForm", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(4, QtGui.QApplication.translate("SocketForm", "10000", None, QtGui.QApplication.UnicodeUTF8))
        self.repeatTimesCbx.setItemText(5, QtGui.QApplication.translate("SocketForm", "100000", None, QtGui.QApplication.UnicodeUTF8))
        self.hexModeCkb.setText(QtGui.QApplication.translate("SocketForm", "十六进制模式", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanBtn.setText(QtGui.QApplication.translate("SocketForm", "清空", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setToolTip(QtGui.QApplication.translate("SocketForm", "<html><head/><body><p>Ctrl+Enter</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setText(QtGui.QApplication.translate("SocketForm", "发送", None, QtGui.QApplication.UnicodeUTF8))

