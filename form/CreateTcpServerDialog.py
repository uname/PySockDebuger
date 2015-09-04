#-*- coding: utf-8 -*-
import utils
import signals
from ui.Ui_CreateTcpServerForm import Ui_CreateTcpServerForm
from PyQt4 import QtGui
from PyQt4 import QtCore

class CreateTcpServerDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_CreateTcpServerForm()
        self.ui.setupUi(self)
		
        self.setModal(True)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
        
    def onOkBtnClicked(self):
        strPort = utils.qstr2str(self.ui.portCmbBox.currentText())
        if not strPort.isdigit():
            return
            
        port = int(strPort)
        if not utils.isPortOk(port):
            return
        
        self.emit(signals.SIG_CREATE_TCP_SERVER, port)
        self.close()
	