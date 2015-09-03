# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_tcp_server_form.ui'
#
# Created: Thu Sep 03 23:23:30 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CreateTcpServerForm(object):
    def setupUi(self, CreateTcpServerForm):
        CreateTcpServerForm.setObjectName(_fromUtf8("CreateTcpServerForm"))
        CreateTcpServerForm.resize(344, 147)
        self.gridLayout = QtGui.QGridLayout(CreateTcpServerForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(CreateTcpServerForm)
        self.label.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.portCmbBox = QtGui.QComboBox(CreateTcpServerForm)
        self.portCmbBox.setEditable(True)
        self.portCmbBox.setObjectName(_fromUtf8("portCmbBox"))
        self.horizontalLayout.addWidget(self.portCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okBtn = QtGui.QPushButton(CreateTcpServerForm)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.cancelBtn = QtGui.QPushButton(CreateTcpServerForm)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.retranslateUi(CreateTcpServerForm)
        QtCore.QMetaObject.connectSlotsByName(CreateTcpServerForm)

    def retranslateUi(self, CreateTcpServerForm):
        CreateTcpServerForm.setWindowTitle(QtGui.QApplication.translate("CreateTcpServerForm", "创建TCP服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreateTcpServerForm", "监听端口", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setText(QtGui.QApplication.translate("CreateTcpServerForm", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("CreateTcpServerForm", "取消", None, QtGui.QApplication.UnicodeUTF8))

