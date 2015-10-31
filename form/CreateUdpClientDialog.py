#-*- coding: utf-8 -*-
import utils
import signals
import config
import error
from ui.Ui_CreateUdpClientForm import Ui_CreateUdpClientForm
from PyQt4 import QtGui
from PyQt4 import QtCore

class CreateUdpClientDialog(QtGui.QDialog):
	
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_CreateUdpClientForm()
        self.ui.setupUi(self)
        self.initIpList()
        self.setModal(True)
        self.setupSignals()
    
    def initIpList(self):
        self.ui.ipCmbBox.addItems(config.DEFAULT_SERVER_IP_LIST + utils.getLocalIpList())
        
    def setupSignals(self):
        self.ui.okBtn.clicked.connect(self.onOkBtnClicked)
        self.ui.broadcastBtn.clicked.connect(self.onBroadcastBtnClicked)
        self.ui.cancelBtn.clicked.connect(self.close)
        self.ui.sysPortCbx.stateChanged.connect(self.onSysPortStateChanged)
        
    def onOkBtnClicked(self):
        strRemotePort = utils.qstr2str(self.ui.remotePortCmbBox.currentText())
        strLocalPort = utils.qstr2str(self.ui.localPortCmbBox.currentText())
        localPort = 0
        if not self.ui.sysPortCbx.isChecked():
            if not strLocalPort.isdigit():
                return
            localPort = int(strLocalPort)
            if not utils.isPortOk(localPort):
                return
            
        if not strRemotePort.isdigit():
            return
            
        remotePort = int(strRemotePort)
        if not utils.isPortOk(remotePort):
            return
        
        self.emit(signals.SIG_CREATE_UDP_CLIENT, utils.qstr2str(self.ui.ipCmbBox.currentText()), remotePort, localPort)
        self.close()
	
    def onBroadcastBtnClicked(self):
        curIp = utils.qstr2str(self.ui.ipCmbBox.currentText())
        if curIp in ("127.0.0.1", "0.0.0.0"):
            return
        
        broadcastIp = utils.getBroadcastIp(curIp)
        if broadcastIp is None:
            return
        
        self.ui.ipCmbBox.setEditText(broadcastIp)
        
    def onSysPortStateChanged(self, state):
        self.ui.localPortCmbBox.setEnabled(state == 0)
        
    def show_(self):
        if self.ui.localPortCmbBox.currentText() == "":
            self.ui.localPortCmbBox.setEditText(`utils.randomPort()`)
        
        self.ui.remotePortCmbBox.setFocus()
        self.show()