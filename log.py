#-*- coding: utf-8 -*-
import config
import logging
import sys

logger = logging.getLogger("root")
__formatter = logging.Formatter("[%(levelname)-7s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s", "%d %b %Y %H:%M:%S")

if config.RELEASE_TYPE == "py":
    __streamHandler = logging.StreamHandler(sys.stdout)
    __streamHandler.setFormatter(__formatter)
    logger.addHandler(__streamHandler)
    
__fileHandler = logging.FileHandler("debug.log")
__fileHandler.setFormatter(__formatter)
logger.addHandler(__fileHandler)

logger.setLevel(logging.DEBUG)
