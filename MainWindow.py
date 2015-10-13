#-*- coding: utf-8 -*-
from PyQt4 import QtGui
import config
import error
import signals
from log import logger
from ui.Ui_MainWindow import Ui_MainWindow
from form.TipPupup import TipPupup
from SigObject import sigObject
from presenter.MainWindowPresenter import MainWindowPresenter

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setupUi()
        self.tipPupup = TipPupup()
        self.presenter = MainWindowPresenter(self)
        self.setupSignals()
    
    def setupUi(self):
        self.ui.setupUi(self)
        self.ui.sockTree.init()
        
    def setupSignals(self):
        self.ui.createBtn.clicked.connect(self.onCreateBtnClicked)
        self.ui.removeBtn.clicked.connect(self.onRemoveBtnClicked)
        self.ui.githubBtn.clicked.connect(self.onGithubBtnClicked)
        self.ui.sockTree.itemClicked.connect(self.onSockItemClicked)
        self.ui.sockTab.currentChanged.connect(self.onSockTabClicked)
        self.connect(sigObject, signals.SIG_REMOTE_TCP_CLIENT_CONNECTED, self.onRemoteTcpClientConnected)
        self.connect(sigObject, signals.SIG_REMOTE_CLOSED, self.onRemoteClosed)
        self.connect(sigObject, signals.SIG_DATA_RECVED, self.onDataRecved)
        
        self.connect(self.presenter.createTcpServerDialog, signals.SIG_CREATE_TCP_SERVER, self.onCreateTcpServer)
        self.connect(self.presenter.createTcpClientDialog, signals.SIG_CREATE_TCP_CLIENT, self.onCreateTcpClient)
    
    def onCreateTcpServer(self, ip, port):
        self.presenter.createTcpServer(ip, port)
    
    def onCreateTcpClient(self, ip, port):
        self.presenter.createTcpClient(ip, port)
        
    def onDataRecved(self, _id, parentId, data):
        logger.debug("id=%d, parentId=%d, data=%s" % (_id, parentId, data))
        self.ui.sockTab.addData(_id, data, config.RECV_TAG)
        
    def onRemoteClosed(self, _id, parentId):
        logger.debug("REMOTE CLOSED")
        self.ui.sockTree.removeSocketItemById(_id)
        self.presenter.removeRemoteTcpClientById(_id, parentId)
        
    def onRemoteTcpClientConnected(self, tcpClient, serverId, _id, address, port):
        self.ui.sockTree.addRemoteTcpClient(serverId, _id, address, port)
        self.ui.sockTab.addRemoteTcpClient(tcpClient, _id, "%s:%d" % (address, port))
        
    def onCreateBtnClicked(self):
        createDialog = self.presenter.getCreateDialog(self.ui.sockTree.currentItem())
        if createDialog is None:
            return
        
        createDialog.show_()
    
    def onSockItemClicked(self, sockItem, i):
        self.presenter.onSockItemClicked(sockItem)
    
    def onSockTabClicked(self, index):
        logger.debug("current sockTab index is %d" % index)
        self.ui.sockTab.clearUnreadIcon(index)
        
    def onGithubBtnClicked(self):
        self.presenter.openGithubSite()
        
    def onRemoveBtnClicked(self):
        sockItem = self.ui.sockTree.currentSockItem()
        self.presenter.removeSocket(sockItem)
        self.ui.sockTree.removeSocketItem(sockItem)
        
    def onCreateTcpServerResult(self, _id, address):
        if _id > 0:
            self.ui.sockTree.addTcpServer(_id, address)
        else:
            self.tipPupup.makeErrorText(error.TCP_CREATE_FAILED)
    
    def onCreateTcpClientResult(self, tcpClient, _id, address):
        if _id > 0:
            self.ui.sockTree.addLocalTcpClient(_id, address)
            self.ui.sockTab.addTcpClient(tcpClient, _id, address)
        else:
            self.tipPupup.makeErrorText(error.TCP_CLIENT_CONNECT_ERROR)
        
    def closeEvent(self, e):
        self.presenter.removeAllSockets()
        e.accept()