# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/socket_form.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SocketForm(object):
    def setupUi(self, SocketForm):
        SocketForm.setObjectName(_fromUtf8("SocketForm"))
        SocketForm.resize(739, 549)
        self.gridLayout_2 = QtGui.QGridLayout(SocketForm)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox = QtGui.QGroupBox(SocketForm)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.connectBtn = QtGui.QPushButton(self.groupBox)
        self.connectBtn.setObjectName(_fromUtf8("connectBtn"))
        self.horizontalLayout_2.addWidget(self.connectBtn)
        self.statusLabel = QtGui.QLabel(self.groupBox)
        self.statusLabel.setMinimumSize(QtCore.QSize(81, 16))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.horizontalLayout_2.addWidget(self.statusLabel)
        spacerItem = QtGui.QSpacerItem(528, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.rxLcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.rxLcdNumber.setObjectName(_fromUtf8("rxLcdNumber"))
        self.horizontalLayout_3.addWidget(self.rxLcdNumber)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txLcdNumber = QtGui.QLCDNumber(self.groupBox)
        self.txLcdNumber.setObjectName(_fromUtf8("txLcdNumber"))
        self.horizontalLayout_3.addWidget(self.txLcdNumber)
        self.resetBytesBtn = QtGui.QPushButton(self.groupBox)
        self.resetBytesBtn.setObjectName(_fromUtf8("resetBytesBtn"))
        self.horizontalLayout_3.addWidget(self.resetBytesBtn)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.repeatTimesCbx = QtGui.QComboBox(self.groupBox)
        self.repeatTimesCbx.setMaximumSize(QtCore.QSize(102, 16777215))
        self.repeatTimesCbx.setEditable(True)
        self.repeatTimesCbx.setObjectName(_fromUtf8("repeatTimesCbx"))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.repeatTimesCbx.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.repeatTimesCbx)
        self.hexModeCkb = QtGui.QCheckBox(self.groupBox)
        self.hexModeCkb.setObjectName(_fromUtf8("hexModeCkb"))
        self.horizontalLayout_3.addWidget(self.hexModeCkb)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(SocketForm)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.recvTextBrowser = QtGui.QTextBrowser(self.splitter)
        self.recvTextBrowser.setFrameShape(QtGui.QFrame.NoFrame)
        self.recvTextBrowser.setObjectName(_fromUtf8("recvTextBrowser"))
        self.sendPlainTextEdit = QtGui.QPlainTextEdit(self.splitter)
        self.sendPlainTextEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.sendPlainTextEdit.setObjectName(_fromUtf8("sendPlainTextEdit"))
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(608, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cleanBtn = QtGui.QPushButton(SocketForm)
        self.cleanBtn.setObjectName(_fromUtf8("cleanBtn"))
        self.horizontalLayout.addWidget(self.cleanBtn)
        self.sendBtn = QtGui.QPushButton(SocketForm)
        self.sendBtn.setObjectName(_fromUtf8("sendBtn"))
        self.horizontalLayout.addWidget(self.sendBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(SocketForm)
        QtCore.QMetaObject.connectSlotsByName(SocketForm)

    def retranslateUi(self, SocketForm):
        SocketForm.setWindowTitle(_translate("SocketForm", "Form", None))
        self.connectBtn.setText(_translate("SocketForm", "PushButton", None))
        self.statusLabel.setText(_translate("SocketForm", "Status", None))
        self.label.setText(_translate("SocketForm", "Rx", None))
        self.label_2.setText(_translate("SocketForm", "Tx", None))
        self.resetBytesBtn.setText(_translate("SocketForm", "清零", None))
        self.label_3.setText(_translate("SocketForm", "重复发送", None))
        self.repeatTimesCbx.setItemText(0, _translate("SocketForm", "1", None))
        self.repeatTimesCbx.setItemText(1, _translate("SocketForm", "10", None))
        self.repeatTimesCbx.setItemText(2, _translate("SocketForm", "100", None))
        self.repeatTimesCbx.setItemText(3, _translate("SocketForm", "1000", None))
        self.repeatTimesCbx.setItemText(4, _translate("SocketForm", "10000", None))
        self.repeatTimesCbx.setItemText(5, _translate("SocketForm", "100000", None))
        self.hexModeCkb.setText(_translate("SocketForm", "十六进制模式", None))
        self.cleanBtn.setText(_translate("SocketForm", "清空", None))
        self.sendBtn.setToolTip(_translate("SocketForm", "<html><head/><body><p>Ctrl+Enter</p></body></html>", None))
        self.sendBtn.setText(_translate("SocketForm", "发送", None))

