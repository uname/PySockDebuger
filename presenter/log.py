#-*- coding: utf-8 -*-
import logging
import sys

logger = logging.getLogger("")
__formatter = logging.Formatter("[%(levelname)-7s][%(asctime)s][%(filename)s:%(lineno)d] %(message)s", "%d %b %Y %H:%M:%S")
__streamHandler = logging.StreamHandler(sys.stderr)
__streamHandler.setFormatter(__formatter)
__fileHandler = logging.FileHandler("debug.log")
__fileHandler.setFormatter(__formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(__streamHandler)
logger.addHandler(__fileHandler)
