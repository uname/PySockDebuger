#-*- coding: utf-8 -*-
import config
import socket
import random

qstr2str = lambda qstr: qstr.toUtf8().data()
qstr2gbk = lambda qstr: qstr2str(qstr).decode("utf-8").encode("gbk")
isPortOk = lambda port: port > 0 and port < 65535
getLocalIpList = lambda: socket.gethostbyname_ex(socket.gethostname())[2]
randomPort = lambda: random.randint(config.RANDOM_MIN_PORT, config.RANDOM_MAX_PORT)