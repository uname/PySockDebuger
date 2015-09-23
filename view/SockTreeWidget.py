#-*- coding: utf-8 -*-
from log import logger
from ui.AppIcons import *
from SockTreeItem import SockTreeItem
from net import socktypes
import config

from PyQt4.QtGui import (
    QTreeWidget,
    QIcon )

class SockTreeWidget(QTreeWidget):
    
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)
        self.sockItemDict = {}
    
    def init(self):
        tcpServerEntry = SockTreeItem(socktypes.TCP_SERVER, config.TCP_SERVER_ENTRY_TEXT, config.TCP_SERVER_ROOT_ID)
        tcpClientEntry = SockTreeItem(socktypes.TCP_CLIENT_LOCAL, config.TCP_CLIENT_ENTRY_TEXT, config.TCP_CLIENT_ROOT_ID)
        self.addTopLevelItem (tcpServerEntry)
        self.addTopLevelItem (tcpClientEntry)
        self.setCurrentItem(tcpServerEntry)
    
    def getBaseTcpServerItem(self):
        n = self.topLevelItemCount()
        if n < 1:
            logger.error("top level item count is 0!!")
            return
        
        sockItem = None
        for i in xrange(n):
            sockItem = self.topLevelItem(i)
            if sockItem.getBaseSockType() == socktypes.TCP_SERVER_BASE_TYPE:
                break
        
        return sockItem
   
    def getBaseTcpClientItem(self):
        pass
    
    def addRemoteTcpClient(self, serverId, _id, address, port):
        parentItem = self.getSockItemById(serverId)
        if parentItem is None:
            logger.error("parentItem is None")
            return
        
        item = SockTreeItem(socktypes.TCP_CLIENT_REMOTE, "%s:%d" % (address, port), _id, config.TCP_CLIENT_ICON)
        self.sockItemDict[_id] = item
        parentItem.addChild(item)
        self.setItemExpanded(parentItem, True)
        self.setCurrentItem(item)

    def addTcpServer(self, _id, address):
        tcpServerItem = self.getBaseTcpServerItem()
        if not tcpServerItem:
            logger.error("currentItem is None")
            return
            
        item = SockTreeItem(socktypes.TCP_SERVER, address, _id, config.TCP_SERVER_ICON)
        self.sockItemDict[_id] = item
        tcpServerItem.addChild(item)
        self.setItemExpanded(tcpServerItem, True)
        self.setCurrentItem(item)
    
    def getSockItemById(self, _id):
        return self.sockItemDict.get(_id)
        
    def currentSockItem(self):
        return self.currentItem()
        
    def removeSocketItem(self, sockItem):
        parent = sockItem.parent()
        if parent is None:
            return
            
        parent.removeChild(sockItem)
    
    def removeSocketItemById(self, _id):
        sockItem = self.sockItemDict.get(_id)
        if sockItem is None:
            logger.error("sockItem is None, _id = %d" % _id)
            return
        
        self.removeSocketItem(sockItem)
        