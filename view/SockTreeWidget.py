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
    
    def init(self):
        tcpServerEntry = SockTreeItem(socktypes.TCP_SERVER, config.TCP_SERVER_ENTRY_TEXT)
        tcpClientEntry = SockTreeItem(socktypes.TCP_CLIENT_LOCAL, config.TCP_CLIENT_ENTRY_TEXT)
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
        
    def addTcpServer(self, id, address):
        tcpServerItem = self.getBaseTcpServerItem()
        if not tcpServerItem:
            logger.error("currentItem is None")
            return
            
        item = SockTreeItem(socktypes.TCP_CLIENT_REMOTE, address, id, config.TCP_SERVER_ICON)
        tcpServerItem.addChild(item)
        self.setItemExpanded(tcpServerItem, True)
        self.setCurrentItem(item)
    
    def currentSockItem(self):
        return self.currentItem()
        
    def removeSocketItem(self, sockItem):
        sockType = sockItem.getSockType()