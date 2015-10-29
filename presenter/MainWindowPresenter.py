#-*- coding: utf-8 -*-
import utils
import config
import signals
from webbrowser import open as openweb
from log import logger
from form.CreateTcpServerDialog import CreateTcpServerDialog
from form.CreateTcpClientDialog import CreateTcpClientDialog
from form.CreateUdpClientDialog import CreateUdpClientDialog
from net import socktypes
from net.TcpServerManager import tcpServerManager
from net.TcpClientManager import tcpClientManager
from net.UdpClientManager import udpClientManager

class MainWindowPresenter(object):
    
    def __init__(self, window):
        self.window = window
        self.createTcpServerDialog = CreateTcpServerDialog(window)
        self.createTcpClientDialog = CreateTcpClientDialog(window)
        self.createUdpClientDialog = CreateUdpClientDialog(window)
        self.createDialogDict = { socktypes.TCP_SERVER_BASE_TYPE: self.createTcpServerDialog,
                                  socktypes.TCP_CLIENT_BASE_TYPE: self.createTcpClientDialog,
                                  socktypes.UDP_CLIENT_BASE_TYPE: self.createUdpClientDialog }
    
    def getCreateDialog(self, selectedItem):
        baseSockType = selectedItem.getBaseSockType()
        if not self.createDialogDict.has_key(baseSockType):
            logger.error("baseSockType error")
            return
        
        return self.createDialogDict[baseSockType]
    
    def createTcpServer(self, ip, port):
        logger.debug("create tcp server on %s:%d" % (ip, port))
        _id, address = tcpServerManager.create(ip, port)
        self.window.onCreateTcpServerResult(_id, address)
    
    def createTcpClient(self, ip, port):
        logger.debug("create tcp client, server: %s:%d" % (ip, port))
        tcpClient, _id, address = tcpClientManager.create(ip, port)
        self.window.onCreateTcpClientResult(tcpClient, _id, address)
    
    def createUdpClient(self, ip, remoteIp, localIp):
        logger.debug("create udp client: %s:%d, %d" % (ip, remoteIp, localIp))
        udpClient, _id, address = udpClientManager.create(ip, remoteIp)
        self.window.onCreateUdpClientResult(udpClient, _id, address)
        
    def onSockItemClicked(self, sockItem):
        self.window.ui.sockTab.setCurrentSocketFormById(sockItem.getId())
    
    def removeAllSockets(self):
        tcpServerManager.removeAllTcpSevrer()
        tcpClientManager.removeAllClient()
        udpClientManager.removeAllClient()
        # TODO: remove others
    
    def removeRemoteTcpClientById(self, _id, parentId):
        tcpServerManager.removeRemoteClient(_id, parentId)
        self.window.ui.sockTab.removeFormById(_id)
    
    def removeSockTabById(self, _id=None):
        sockItem = 0
        if _id is None:
            sockItem = self.window.ui.sockTree.currentSockItem()
        else:
            sockItem = self.window.ui.sockTree.getSockItemById(_id)
            
        self.removeSocket(sockItem)
        self.window.ui.sockTree.removeSocketItem(sockItem)
        
    def removeSocket(self, sockItem):
        _id = sockItem.getId()
        if _id < 0:
            return
            
        parentId = sockItem.getParentId()
        sockType = sockItem.getSockType()
        logger.debug("sockType --> %d, _id=%d, parentId=%d" % (sockType, _id, parentId))
        if sockType == socktypes.TCP_CLIENT_REMOTE:
            tcpServerManager.removeRemoteClient(_id, parentId)
            self.window.ui.sockTab.removeFormById(_id)
            
        elif sockType == socktypes.TCP_SERVER:
            logger.debug("remove tcp server")
            tcpServerManager.removeServer(_id)
            
        elif sockType == socktypes.TCP_CLIENT_LOCAL:
            tcpClientManager.removeClient(_id)
            self.window.ui.sockTab.removeFormById(_id)
        
        elif sockType == socktypes.UDP_CLIENT_LOCAL:
            logger.debug("remove udp client")
            udpClientManager.removeClient(_id)
            self.window.ui.sockTab.removeFormById(_id)
            
        else:
            pass
            
    def openGithubSite(self):
        openweb(config.GITHUB_HOME)
        