# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_tcp_client_form.ui'
#
# Created: Fri Sep 04 00:20:19 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        self.comboBox = QtGui.QComboBox(CreateTcpClientForm)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_3.addWidget(self.comboBox)
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
        CreateTcpClientForm.setWindowTitle(QtGui.QApplication.translate("CreateTcpClientForm", "创建TCP客户端", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreateTcpClientForm", "对方地址", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreateTcpClientForm", "对方端口", None, QtGui.QApplication.UnicodeUTF8))
        self.okBtn.setText(QtGui.QApplication.translate("CreateTcpClientForm", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("CreateTcpClientForm", "取消", None, QtGui.QApplication.UnicodeUTF8))

