# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/socket_form.ui'
#
# Created: Fri Sep 25 14:26:00 2015
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
        self.recvTextBrowser.setFrameShape(QtGui.QFrame.Box)
        self.recvTextBrowser.setObjectName(_fromUtf8("recvTextBrowser"))
        self.sendPlainTextEdit = QtGui.QPlainTextEdit(self.splitter)
        self.sendPlainTextEdit.setFrameShape(QtGui.QFrame.Box)
        self.sendPlainTextEdit.setObjectName(_fromUtf8("sendPlainTextEdit"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(608, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sendBtn = QtGui.QPushButton(SocketForm)
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.horizontalLayout.addWidget(self.sendBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(SocketForm)
        QtCore.QMetaObject.connectSlotsByName(SocketForm)

    def retranslateUi(self, SocketForm):
        SocketForm.setWindowTitle(QtGui.QApplication.translate("SocketForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.sendBtn.setText(QtGui.QApplication.translate("SocketForm", "发送", None, QtGui.QApplication.UnicodeUTF8))

