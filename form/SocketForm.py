#-*- coding: utf-8 -*-
from ui.Ui_SocketForm import Ui_SocketForm
from PyQt4.QtGui import QWidget

class SocketForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_SocketForm()
        self.ui.setupUi(self)