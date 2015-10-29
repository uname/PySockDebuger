#-*- coding: utf-8 -*-
from PyQt4 import QtGui
from ui.AppIcons import *
import config
from net import socktypes
from form.SocketForm import SocketForm

class SockTab(QtGui.QTabWidget):
    
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        self.forms = [{"id": 0}]
        
    def addSockForm(self, tcpClient, _id, label, iconSet):
        form = SocketForm(tcpClient, self)
        self.addTab(form, QtGui.QIcon(iconSet[0]), label)
        self.setCurrentIndex(self.count() - 1)
        self.forms.append({"id": _id, "form": form, "iconSet": iconSet, "unread": False})
        
    def addRemoteTcpClient(self, tcpClient, _id, label):
        self.addSockForm(tcpClient, _id, label, config.TCP_CLIENT_ICON_REMOTE_SET)
    
    def addTcpClient(self, tcpClient, _id, label):
        self.addSockForm(tcpClient, _id, label, config.TCP_CLIENT_ICON_LOCAL_SET)
    
    def addUdpClient(self, udpClient, _id, label):
        self.addSockForm(udpClient, _id, label, config.UDP_CLIENT_ICON_LOCAL_SET)
        
    def getIndexById(self, _id):
        index = 0
        for infoDict in self.forms:
            if infoDict["id"] == _id:
                break
            index += 1
        
        if index == len(self.forms):
            return -1
        
        return index
    
    def clearUnreadIcon(self, index):
        if index < 1 or index >= len(self.forms):
            return
            
        if self.forms[index]["unread"]:
            self.forms[index]["unread"] = False
            self.setTabIcon(index, QtGui.QIcon(self.forms[index]["iconSet"][0]))
        
    def removeFormById(self, _id):
        index = self.getIndexById(_id)
        if index < 0:
            return
        self.removeTab(index)
        self.forms.pop(index)
        
    def setCurrentSocketFormById(self, _id):
        index = self.getIndexById(_id)
        if index < 0:
            return
        
        self.setCurrentIndex(index + 1)
    
    def addData(self, _id, data, tag=""):
        index = self.getIndexById(_id)
        if index < 0:
            return
            
        form = self.forms[index]["form"]
        form.addData(data, tag)
        if index != self.currentIndex():
            self.forms[index]["unread"] = True
            self.setTabIcon(index, QtGui.QIcon(self.forms[index]["iconSet"][1]))
            