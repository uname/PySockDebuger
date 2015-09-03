#-*- coding: utf-8 -*-
import utils
import config
from form.CreateTcpServerDialog import CreateTcpServerDialog
from form.CreateTcpClientDialog import CreateTcpClientDialog

class MainWindowPresenter(object):
    
    def __init__(self, window):
        self.CREATE_DIALOG_LIST = [CreateTcpServerDialog(window),
                                   CreateTcpClientDialog(window)]
    
    def getCreateType(self, selectedItem):
        if selectedItem is None:
            return
        
        typeText = utils.qstr2str(selectedItem.text(0))
        try:
            return config.CREATE_TYPES.index(typeText)
        except ValueError as e:
            pass
    
    def getCreateDialog(self, selectedItem):
        typeIndex = self.getCreateType(selectedItem)
        if typeIndex is None:
            return
        
        if typeIndex < 0 or typeIndex >= len(self.CREATE_DIALOG_LIST):
            return
        
        return self.CREATE_DIALOG_LIST[typeIndex]
        