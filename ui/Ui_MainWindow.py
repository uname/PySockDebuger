# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main_window.ui'
#
# Created: Thu Sep 03 23:36:59 2015
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
        MainWindow.resize(777, 523)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 754, 43))
        self.frame.setMaximumSize(QtCore.QSize(761, 16777215))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.createBtn = QtGui.QPushButton(self.frame)
        self.createBtn.setObjectName(_fromUtf8("createBtn"))
        self.gridLayout.addWidget(self.createBtn, 0, 0, 1, 1)
        self.removeBtn = QtGui.QPushButton(self.frame)
        self.removeBtn.setObjectName(_fromUtf8("removeBtn"))
        self.gridLayout.addWidget(self.removeBtn, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(488, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.aboutBtn = QtGui.QPushButton(self.frame)
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.gridLayout.addWidget(self.aboutBtn, 0, 3, 1, 1)
        self.sockTypeTree = QtGui.QTreeWidget(self.centralwidget)
        self.sockTypeTree.setGeometry(QtCore.QRect(10, 60, 171, 401))
        self.sockTypeTree.setStyleSheet(_fromUtf8(""))
        self.sockTypeTree.setObjectName(_fromUtf8("sockTypeTree"))
        item_0 = QtGui.QTreeWidgetItem(self.sockTypeTree)
        item_0 = QtGui.QTreeWidgetItem(self.sockTypeTree)
        self.sockTab = QtGui.QTabWidget(self.centralwidget)
        self.sockTab.setGeometry(QtCore.QRect(190, 60, 571, 401))
        self.sockTab.setObjectName(_fromUtf8("sockTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.sockTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.sockTab.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 23))
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
        self.createBtn.setText(QtGui.QApplication.translate("MainWindow", "创建", None, QtGui.QApplication.UnicodeUTF8))
        self.removeBtn.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutBtn.setText(QtGui.QApplication.translate("MainWindow", "关于", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.sockTypeTree.isSortingEnabled()
        self.sockTypeTree.setSortingEnabled(False)
        self.sockTypeTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "TCP服务器", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTypeTree.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "TCP客户端", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTypeTree.setSortingEnabled(__sortingEnabled)
        self.sockTab.setTabText(self.sockTab.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.sockTab.setTabText(self.sockTab.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

