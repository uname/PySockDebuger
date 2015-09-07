#-*- coding: utf-8 -*-
from PyQt4 import QtGui
import config
from ui.Ui_MainWindow import Ui_MainWindow
from presenter.MainWindowPresenter import MainWindowPresenter

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.presenter = MainWindowPresenter(self)
        self.setupSignals()
        
    def setupSignals(self):
        self.ui.createBtn.clicked.connect(self.onCreateBtnClicked)
        
    def onCreateBtnClicked(self):
        createDialog = self.presenter.getCreateDialog(self.ui.sockTypeTree.currentItem())
        if createDialog is None:
            return
        
        createDialog.show()
    
    def onCreateTcpServerOK(self, address):
        print "OK!"
        
    def closeEvent(self, e):
        self.presenter.closeAllSockets()
        e.accept()