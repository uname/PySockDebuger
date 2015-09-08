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
        
    def addTcpServer(self, address):
        curItem = self.currentItem()
        if not curItem:
            logger.error("currentItem is None")
            return
            
        item = SockTreeItem(socktypes.TCP_CLIENT_REMOTE, address, config.TCP_SERVER_ICON)
        curItem.addChild(item)
        self.setItemExpanded(curItem, True)
        self.setCurrentItem(item)
        