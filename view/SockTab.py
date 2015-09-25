#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from form.SocketForm import SocketForm

class SockTab(QtGui.QTabWidget):
    
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        self.forms = []
    
    def addRemoteTcpClient(self, _id, label):
        form = SocketForm(self)
        self.addTab(form, label)
        self.setCurrentIndex(self.count() - 1)
        self.forms.append((_id, form))
    
    def getIndexById(self, _id):
        index = 0
        for id_, _ in self.forms:
            if id_ == _id:
                break
            index += 1
        
        if index == len(self.forms):
            return -1
        
        return index
        
    def removeFormById(self, _id):
        index = self.getIndexById(_id)
        if index < 0:
            return
        self.removeTab(index + 1)
        self.forms.pop(index)
        
    def setCurrentSocketFormById(self, _id):
        index = self.getIndexById(_id)
        if index < 0:
            return
        
        self.setCurrentIndex(index + 1)
