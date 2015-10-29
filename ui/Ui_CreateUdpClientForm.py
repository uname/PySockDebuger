# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_udp_client_form.ui'
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

class Ui_CreateUdpClientForm(object):
    def setupUi(self, CreateUdpClientForm):
        CreateUdpClientForm.setObjectName(_fromUtf8("CreateUdpClientForm"))
        CreateUdpClientForm.resize(344, 193)
        self.gridLayout = QtGui.QGridLayout(CreateUdpClientForm)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(CreateUdpClientForm)
        self.label_2.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.ipCmbBox = QtGui.QComboBox(CreateUdpClientForm)
        self.ipCmbBox.setEditable(True)
        self.ipCmbBox.setObjectName(_fromUtf8("ipCmbBox"))
        self.horizontalLayout_3.addWidget(self.ipCmbBox)
        self.broadcastBtn = QtGui.QPushButton(CreateUdpClientForm)
        self.broadcastBtn.setMaximumSize(QtCore.QSize(75, 16777215))
        self.broadcastBtn.setObjectName(_fromUtf8("broadcastBtn"))
        self.horizontalLayout_3.addWidget(self.broadcastBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(CreateUdpClientForm)
        self.label.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.remotePortCmbBox = QtGui.QComboBox(CreateUdpClientForm)
        self.remotePortCmbBox.setEditable(True)
        self.remotePortCmbBox.setObjectName(_fromUtf8("remotePortCmbBox"))
        self.horizontalLayout.addWidget(self.remotePortCmbBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(CreateUdpClientForm)
        self.label_4.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(CreateUdpClientForm)
        self.label_3.setMaximumSize(QtCore.QSize(54, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.localPortCmbBox = QtGui.QComboBox(CreateUdpClientForm)
        self.localPortCmbBox.setEditable(True)
        self.localPortCmbBox.setObjectName(_fromUtf8("localPortCmbBox"))
        self.horizontalLayout_4.addWidget(self.localPortCmbBox)
        self.sysPortCbx = QtGui.QCheckBox(CreateUdpClientForm)
        self.sysPortCbx.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sysPortCbx.setObjectName(_fromUtf8("sysPortCbx"))
        self.horizontalLayout_4.addWidget(self.sysPortCbx)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 29, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(68, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.okBtn = QtGui.QPushButton(CreateUdpClientForm)
        self.okBtn.setDefault(True)
        self.okBtn.setObjectName(_fromUtf8("okBtn"))
        self.horizontalLayout_2.addWidget(self.okBtn)
        self.cancelBtn = QtGui.QPushButton(CreateUdpClientForm)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout_2.addWidget(self.cancelBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 2)

        self.retranslateUi(CreateUdpClientForm)
        QtCore.QMetaObject.connectSlotsByName(CreateUdpClientForm)

    def retranslateUi(self, CreateUdpClientForm):
        CreateUdpClientForm.setWindowTitle(_translate("CreateUdpClientForm", "创建UDP客户端", None))
        self.label_2.setText(_translate("CreateUdpClientForm", "对方地址", None))
        self.broadcastBtn.setText(_translate("CreateUdpClientForm", "广播地址", None))
        self.label.setText(_translate("CreateUdpClientForm", "对方端口", None))
        self.label_3.setText(_translate("CreateUdpClientForm", "本地端口", None))
        self.sysPortCbx.setText(_translate("CreateUdpClientForm", "系统分配", None))
        self.okBtn.setText(_translate("CreateUdpClientForm", "确定", None))
        self.cancelBtn.setText(_translate("CreateUdpClientForm", "取消", None))

