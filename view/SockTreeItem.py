#-*- coding: utf-8 -*-
from PyQt4.QtGui import QTreeWidgetItem, QIcon

class SockTreeItem(QTreeWidgetItem):
    
    def __init__(self, sockType, name, _id=0, icon=None):
        QTreeWidgetItem.__init__(self)
        self.sockType = sockType
        self.name = name
        self._id = _id
        self.setText(0, name)
        if icon:
            self.setIcon(0, QIcon(icon))
            
    def getBaseSockType(self):
        return self.getSockType() & 0xf0
    
    def getSockType(self):
        return self.sockType