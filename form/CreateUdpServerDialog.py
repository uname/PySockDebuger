#-*- coding: utf-8 -*-
import signals
from CreateTcpServerDialog import CreateTcpServerDialog

class CreateUdpServerDialog(CreateTcpServerDialog):
    
    def __init__(self, parent=None):
        CreateTcpServerDialog.__init__(self, parent)
        self.okSig = signals.SIG_CREATE_UDP_SERVER
        self.setWindowTitle(u"创建UDP服务器")
        