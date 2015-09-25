# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main_window.ui'
#
# Created: Fri Sep 25 14:53:27 2015
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
        self.sockTree = SockTreeWidget(self.centralwidget)
        self.sockTree.setGeometry(QtCore.QRect(10, 60, 231, 541))
        self.sockTree.setMinimumSize(QtCore.QSize(201, 0))
        self.sockTree.setStyleSheet(_fromUtf8(""))
        self.sockTree.setObjectName(_fromUtf8("sockTree"))
        self.sockTab = SockTab(self.centralwidget)
        self.sockTab.setGeometry(QtCore.QRect(250, 60, 721, 541))
        self.sockTab.setObjectName(_fromUtf8("sockTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 511, 91))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.sockTab.addTab(self.tab, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 961, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.createBtn = QtGui.QPushButton(self.widget)
        self.createBtn.setObjectName(_fromUtf8("createBtn"))
        self.horizontalLayout.addWidget(self.createBtn)
        self.removeBtn = QtGui.QPushButton(self.widget)
        self.removeBtn.setObjectName(_fromUtf8("removeBtn"))
        self.horizontalLayout.addWidget(self.removeBtn)
        spacerItem = QtGui.QSpacerItem(668, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.githubBtn = QtGui.QPushButton(self.widget)
        self.githubBtn.setMaximumSize(QtCore.QSize(121, 16777215))
        self.githubBtn.setObjectName(_fromUtf8("githubBtn"))
        self.horizontalLayout.addWidget(self.githubBtn)
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email ehcapa@qq.com</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTab.setTabText(self.sockTab.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.createBtn.setText(QtGui.QApplication.translate("MainWindow", "创建", None, QtGui.QApplication.UnicodeUTF8))
        self.removeBtn.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.githubBtn.setText(QtGui.QApplication.translate("MainWindow", "Fork on Github", None, QtGui.QApplication.UnicodeUTF8))

from view.SockTab import SockTab
from view.SockTreeWidget import SockTreeWidget
