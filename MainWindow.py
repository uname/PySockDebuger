#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
