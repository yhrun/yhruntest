#!/Users/yhrun/workspace/MyEnv/bin/python
#coding=utf-8
import os
import re
import sys
import time
import json

def Runtime(function):
    def _fun(*args):
        start = time.time()
        res = function(*args)
        end = time.time()
        print 'run time : ',str(end-start)
        return res
    return _fun

@Runtime
def Fun():
    time.sleep(1)

class Test():
    def __init__(self):
        self.__test = 0

def Error():
    try:
        ss = '{}'
        json.loads(ss)
    except BaseException as e:
        print e.message
    else:
        print 'else'
    finally:
        print 'finish'

if __name__ == '__main__':
    Error()


