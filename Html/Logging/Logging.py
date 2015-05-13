#coding=utf-8
#Author : Yhrun
#Mail   : yhruner@gmail.com

import os
import sys
import json
import logging
import logging.handlers

formate = logging.Formatter("[%(asctime)s %(filename)s %(funcName)s %(lineno)s %(levelname)s] %(message)s")

logging.basicConfig(level=logging.DEBUG,
                format="[%(asctime)s %(filename)s %(funcName)s %(lineno)s %(levelname)s] %(message)s",
                datefmt='%a, %d %b %Y %H:%M:%S')

info = logging.getLogger('info')
warn = logging.getLogger('warn')
debug = logging.getLogger('debug')

info.setLevel(logging.INFO)
warn.setLevel(logging.WARNING)
debug.setLevel(logging.DEBUG)

path = os.path.join(os.path.dirname(__file__),'Log')
print path
if not os.path.isdir(path):
    os.mkdir(path)
#if os.path.isdir("")

res1 = logging.handlers.TimedRotatingFileHandler(os.getcwd()+'/Log/info.log','D',1,0)
res2 = logging.handlers.TimedRotatingFileHandler(os.getcwd()+'/Log/warn.log','D',1,0)
res3 = logging.handlers.TimedRotatingFileHandler(os.getcwd()+'/Log/debug.log','D',1,0)

res1.setLevel(logging.INFO)
res1.setFormatter(formate)

res2.setLevel(logging.WARN)
res2.setFormatter(formate)

res3.setLevel(logging.DEBUG)
res3.setFormatter(formate)

info.addHandler(res1)
warn.addHandler(res2)
debug.addHandler(res3)

if __name__ == '__main__':
    #logging.getLogger('info').info('this is a test')
    #logging.getLogger('warn').warn('this is a test')
    #logging.getLogger('debug').debug('this is a test')
    logging.debug('this is a test')