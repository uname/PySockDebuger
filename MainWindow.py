#-*- coding: utf-8 -*-
from PyQt4 import QtGui
import config
import error
from ui.Ui_MainWindow import Ui_MainWindow
from form.TipPupup import TipPupup
from presenter.MainWindowPresenter import MainWindowPresenter

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.tipPupup = TipPupup()
        self.presenter = MainWindowPresenter(self)
        self.setupSignals()
    
    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.sockTree.init()
        
    def setupSignals(self):
        self.ui.createBtn.clicked.connect(self.onCreateBtnClicked)
        self.ui.removeBtn.clicked.connect(self.onRemoveBtnClicked)
        
    def onCreateBtnClicked(self):
        createDialog = self.presenter.getCreateDialog(self.ui.sockTree.currentItem())
        if createDialog is None:
            return
        
        createDialog.show()
    
    def onRemoveBtnClicked(self):
        sockItem = self.ui.sockTree.currentSockItem()
        self.presenter.removeSocket(sockItem)
        self.ui.sockTree.removeSocketItem(sockItem)
        
    def onCreateTcpServerResult(self, _id, address):
        if _id != 0:
            self.ui.sockTree.addTcpServer(_id, address)
        else:
            self.tipPupup.makeErrorText(error.TCP_CREATE_FAILED)
        
    def closeEvent(self, e):
        self.presenter.closeAllSockets()
        e.accept()