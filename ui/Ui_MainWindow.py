# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main_window.ui'
#
# Created: Tue Oct 27 14:34:20 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(985, 664)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.sockTree = SockTreeWidget(self.splitter)
        self.sockTree.setMinimumSize(QtCore.QSize(201, 0))
        self.sockTree.setMaximumSize(QtCore.QSize(350, 16777215))
        self.sockTree.setStyleSheet(_fromUtf8(""))
        self.sockTree.setObjectName(_fromUtf8("sockTree"))
        self.sockTab = SockTab(self.splitter)
        self.sockTab.setMinimumSize(QtCore.QSize(682, 0))
        self.sockTab.setObjectName(_fromUtf8("sockTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 641, 121))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.qrcodeView = QtGui.QPushButton(self.tab)
        self.qrcodeView.setGeometry(QtCore.QRect(10, 160, 277, 310))
        self.qrcodeView.setAutoFillBackground(True)
        self.qrcodeView.setText(_fromUtf8(""))
        self.qrcodeView.setIconSize(QtCore.QSize(277, 310))
        self.qrcodeView.setObjectName(_fromUtf8("qrcodeView"))
        self.sockTab.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.splitter, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createBtn = QtGui.QPushButton(self.centralwidget)
        self.createBtn.setObjectName(_fromUtf8("createBtn"))
        self.horizontalLayout.addWidget(self.createBtn)
        self.removeBtn = QtGui.QPushButton(self.centralwidget)
        self.removeBtn.setObjectName(_fromUtf8("removeBtn"))
        self.horizontalLayout.addWidget(self.removeBtn)
        spacerItem = QtGui.QSpacerItem(668, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.githubBtn = QtGui.QPushButton(self.centralwidget)
        self.githubBtn.setMaximumSize(QtCore.QSize(121, 16777215))
        self.githubBtn.setObjectName(_fromUtf8("githubBtn"))
        self.horizontalLayout.addWidget(self.githubBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(20, 567, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sockTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PySockDebuger", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This is an open source project for TCP &amp; UDP debugging</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/uname/PySockDebuger</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By Qingwei He.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email ehcapa@qq.com</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">In order to help the developer to make better,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">you can donate by scan the QR code below:) Thanks!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTab.setTabText(self.sockTab.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.createBtn.setText(QtGui.QApplication.translate("MainWindow", "创建", None, QtGui.QApplication.UnicodeUTF8))
        self.removeBtn.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.githubBtn.setText(QtGui.QApplication.translate("MainWindow", "Fork on Github", None, QtGui.QApplication.UnicodeUTF8))

from view.SockTab import SockTab
from view.SockTreeWidget import SockTreeWidget
import ExtAppIcons_rc
