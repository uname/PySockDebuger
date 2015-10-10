# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_tcp_client_form.ui'
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

class Ui_CreateTcpClientForm(object):
    def setupUi(self, CreateTcpClientForm):
        CreateTcpClientForm.setObjectName(_fromUtf8("CreateTcpClientForm"))
        CreateTcpClientForm.resize(344, 147)
        self.gridLayout = QtGui.QGridLayout(CreateTcpClientForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(CreateTcpClientForm)
        self.label_2.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.ipCmbBox = QtGui.QComboBox(CreateTcpClientForm)
        self.ipCmbBox.setEditable(True)
        self.ipCmbBox.setObjectName(_fromUtf8("ipCmbBox"))
        self.horizontalLayout_3.addWidget(self.ipCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(CreateTcpClientForm)
        self.label.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portCmbBox = QtGui.QComboBox(CreateTcpClientForm)
        self.portCmbBox.setEditable(True)
        self.portCmbBox.setObjectName(_fromUtf8("portCmbBox"))
        self.horizontalLayout.addWidget(self.portCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okBtn = QtGui.QPushButton(CreateTcpClientForm)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.cancelBtn = QtGui.QPushButton(CreateTcpClientForm)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 2)

        self.retranslateUi(CreateTcpClientForm)
        QtCore.QMetaObject.connectSlotsByName(CreateTcpClientForm)

    def retranslateUi(self, CreateTcpClientForm):
        CreateTcpClientForm.setWindowTitle(_translate("CreateTcpClientForm", "创建TCP客户端", None))
        self.label_2.setText(_translate("CreateTcpClientForm", "对方地址", None))
        self.label.setText(_translate("CreateTcpClientForm", "对方端口", None))
        self.okBtn.setText(_translate("CreateTcpClientForm", "确定", None))
        self.cancelBtn.setText(_translate("CreateTcpClientForm", "取消", None))

