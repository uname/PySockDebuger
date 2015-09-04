#-*- coding: utf-8 -*-

qstr2str = lambda qstr: qstr.toUtf8().data()
isPortOk = lambda port: port > 0 and port < 65535