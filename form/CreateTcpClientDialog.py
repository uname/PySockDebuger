#-*- coding: utf-8 -*-
import config
import utils
import signals
from ui.Ui_CreateTcpClientForm import Ui_CreateTcpClientForm
from form.TipPupup import TipPupup
from PyQt4 import QtGui

class CreateTcpClientDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_CreateTcpClientForm()
        self.ui.setupUi(self)
        self.initIpList()
        self.setModal(True)
        self.setupSignals()
    
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
    
    def initIpList(self):
        self.ui.ipCmbBox.addItems(config.DEFAULT_CLIENT_IP_LIST + utils.getLocalIpList())
        
    def onOkBtnClicked(self):
        strPort = utils.qstr2str(self.ui.portCmbBox.currentText())
        if not strPort.isdigit():
            return
            
        port = int(strPort)
        if not utils.isPortOk(port):
            return
        
        self.emit(signals.SIG_CREATE_TCP_CLIENT, utils.qstr2str(self.ui.ipCmbBox.currentText()), port)
        self.close()
    
    def show_(self):
        self.show()