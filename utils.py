#-*- coding: utf-8 -*-

qstr2str = lambda qstr: qstr.toUtf8().data()
qstr2gbk = lambda qstr: qstr2str(qstr).decode("utf-8").encode("gbk")
isPortOk = lambda port: port > 0 and port < 65535