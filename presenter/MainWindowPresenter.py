#-*- coding: utf-8 -*-
import utils
import config
import signals
from webbrowser import open as openweb
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
    
    def removeAllSockets(self):
        tcpServerManager.removeAllTcpSevrer()
        # TODO: remove others
    
    def removeRemoteTcpClientById(self, _id, parentId):
        tcpServerManager.removeRemoteClient(_id, parentId)
        
    def removeSocket(self, sockItem):
        _id = sockItem.getId()
        if _id < 0:
            return
            
        parentId = sockItem.getParentId()
        sockType = sockItem.getSockType()
        logger.debug("sockType --> %d, _id=%d, parentId=%d" % (sockType, _id, parentId))
        if sockType == socktypes.TCP_CLIENT_REMOTE:
            tcpServerManager.removeRemoteClient(_id, parentId)
            
        elif sockType == socktypes.TCP_SERVER:
            tcpServerManager.removeServer(_id)
        else:
            pass
            
    def openGithubSite(self):
        openweb(config.GITHUB_HOME)
        