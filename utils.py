#-*- coding: utf-8 -*-
import config
import socket
import random

qstr2str = lambda qstr: qstr.toUtf8().data()
qstr2gbk = lambda qstr: qstr2str(qstr).decode("utf-8").encode("gbk")
isPortOk = lambda port: port > 0 and port < 65535
getLocalIpList = lambda: socket.gethostbyname_ex(socket.gethostname())[2]
randomPort = lambda: random.randint(config.RANDOM_MIN_PORT, config.RANDOM_MAX_PORT)


def getMask(ip):
    return "255.255.255.0"  # just for test
    
def getBroadcastIp(ip, mask=None):
    if not isinstance(ip, basestring):
        return
    
    if mask is None:
        mask = getMask(ip)
    
    ipTokens = map(int, ip.split("."))
    maskTokens = map(int, mask.split("."))
    
    return ".".join([`ipTokens[i] & maskTokens[i] | (~maskTokens[i] & 0xff)` for i in xrange(len(ipTokens))])
    
    
def dumpHex(data, addr=0, prefix=""):
        '''
        Utility function that converts data into hex dump format.

        @type  data:   Raw Bytes
        @param data:   Raw bytes to view in hex dump
        @type  addr:   DWORD
        @param addr:   (Optional, def=0) Address to start hex offset display from
        @type  prefix: String (Optional, def="")
        @param prefix: String to prefix each line of hex dump with.

        @rtype:  String
        @return: Hex dump of data.
        '''

        dump  = prefix
        slice = ""

        for byte in data:
            if addr % 16 == 0:
                dump += " "

                for char in slice:
                    if ord(char) >= 32 and ord(char) <= 126:
                        dump += char
                    else:
                        dump += "."

                dump += "\n  %s%04x: " % (prefix, addr)
                slice = ""

            dump  += "%02x " % ord(byte)
            slice += byte
            addr  += 1

        remainder = addr % 16

        if remainder != 0:
            dump += "   " * (16 - remainder) + " "

        for char in slice:
            if ord(char) >= 32 and ord(char) <= 126:
                dump += char
            else:
                dump += "."

        return dump + "\n"