#-*- coding: utf-8 -*-
import utils
import config
import signals
from log import logger
from form.CreateTcpServerDialog import CreateTcpServerDialog
from form.CreateTcpClientDialog import CreateTcpClientDialog
from net.TcpServerManager import tcpServerManager

class MainWindowPresenter(object):
    
    def __init__(self, window):
        self.window = window
        self.createTcpServerDialog = CreateTcpServerDialog(window)
        self.createTcpClientDialog = CreateTcpClientDialog(window)
        self.CREATE_DIALOG_LIST = [ self.createTcpServerDialog,
                                    self.createTcpClientDialog ]
        
        self.setupSignals()
    
    def setupSignals(self):
        self.window.connect(self.createTcpServerDialog, signals.SIG_CREATE_TCP_SERVER, self.onCreateTcpServer)
        
    def getCreateType(self, selectedItem):
        if selectedItem is None:
            return
        
        typeText = utils.qstr2str(selectedItem.text(0))
        try:
            return config.CREATE_TYPES.index(typeText)
        except ValueError as e:
            pass
    
    def getCreateDialog(self, selectedItem):
        typeIndex = self.getCreateType(selectedItem)
        if typeIndex is None:
            return
        
        if typeIndex < 0 or typeIndex >= len(self.CREATE_DIALOG_LIST):
            return
        
        return self.CREATE_DIALOG_LIST[typeIndex]
    
    def onCreateTcpServer(self, port):
        logger.debug("create tcp server on %d" % port)
        address = tcpServerManager.create(port)
        if not address:
            return
        
        self.window.onCreateTcpServerOK(address)
    
    def closeAllSockets(self):
        tcpServerManager.closeAllTcpSevrer()