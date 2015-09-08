#-*- coding: utf-8 -*-
import utils
import config
import signals
from log import logger
from form.CreateTcpServerDialog import CreateTcpServerDialog
from form.CreateTcpClientDialog import CreateTcpClientDialog
from net import socktypes
from net.TcpServerManager import tcpServerManager

class MainWindowPresenter(object):
    
    def __init__(self, window):
        self.window = window
        self.createTcpServerDialog = CreateTcpServerDialog(window)
        self.createTcpClientDialog = CreateTcpClientDialog(window)
        self.createDialogDict = { socktypes.TCP_SERVER_BASE_TYPE: self.createTcpServerDialog,
                                  socktypes.TCP_CLIENT_BASE_TYPE: self.createTcpClientDialog }
        
        self.setupSignals()
    
    def setupSignals(self):
        self.window.connect(self.createTcpServerDialog, signals.SIG_CREATE_TCP_SERVER, self.onCreateTcpServer)
    
    def getCreateDialog(self, selectedItem):
        baseSockType = selectedItem.getBaseSockType()
        if not self.createDialogDict.has_key(baseSockType):
            logger.error("baseSockType error")
            return
        
        return self.createDialogDict[baseSockType]
    
    def onCreateTcpServer(self, port):
        logger.debug("create tcp server on %d" % port)
        _id, address = tcpServerManager.create(port)
        self.window.onCreateTcpServerResult(_id, address)
    
    def closeAllSockets(self):
        tcpServerManager.closeAllTcpSevrer()
    
    def removeSocket(self, sockItem):
        _id = sockItem.getId()
        tcpServerManager.remove(_id)