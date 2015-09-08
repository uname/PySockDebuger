#-*- coding: utf-8 -*-
from PyQt4.QtGui import QTreeWidgetItem, QIcon

class SockTreeItem(QTreeWidgetItem):
    
    def __init__(self, sockType, text, icon=None):
        QTreeWidgetItem.__init__(self)
        self.sockType = sockType
        self.setText(0, text)
        if icon:
            self.setIcon(0, QIcon(icon))
            
    def getSockType(self):
        return self.sockType & 0xf0
        
    
    