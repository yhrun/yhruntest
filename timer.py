#coding=utf-8
import os
import sys
import threading
import json
from tornado import gen
from tornado import ioloop
from tornado.web import asynchronous, RequestHandler, Application
import tornado
import time
from tornado import httpclient
global count
count = 0

class Test(RequestHandler):
    def get(self):
        self.write(str(count))
        self.finish()

def Server(ip,port):
    api = tornado.web.Application([(r'/test',Test)])
    api.listen(port,ip)
    ioloop.IOLoop.instance().start()

def Timer():
    print 'timer start'
    print 'exe sleep : 5'
    time.sleep(5)
    global count
    count += 1
    t = threading.Timer(2,Timer)
    t.start()
    print 'end'



if __name__ == '__main__':
    #t = threading.Timer(2,Timer)
    #t.start()
    #Server('0.0.0.0','8881')
    print sys.path[0]
