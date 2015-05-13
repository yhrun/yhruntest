#coding=utf-8
import os
import re
import sys
import json
import time
import urllib
import pymongo
from Logging import Logging
import logging
import tornado
from tornado import web,gen
from tornado import options
from tornado.options import define,options

#from Tool import SystemInfo

class Item(object):
    def __init__(self):
        #self.ip = ''
        self.begin_for_day = time.time()
        self.begin_for_hours = time.time()
        self.count_for_day = 1
        self.count_for_hours = 1
        self.status = 0         # 0:normal  1:day error 2:hours error
        self.error_begin = time.time()

class IpTables(object):
    def __init__(self):
        self.info = dict()
        self.H_MAX = 5
        self.D_MAX = 1000
        self.D_TIME = 7*24*3600
        self.H_TIME = 10

    def Check(self,ip):
        if ip not in self.info:
            self.info[ip] = Item()
            #self.info[ip].count_for_day += 1
            #self.info[ip].count_for_hours += 1
        dt = time.time() - self.info[ip].begin_for_day
        ht = time.time() - self.info[ip].begin_for_hours
        et = time.time() - self.info[ip].error_begin

        #print et,self.info[ip].status

        if self.info[ip].status == 1:
            if et < self.D_TIME:return False
            self.info[ip] = Item()
            return True

        if self.info[ip].status == 2:
            print et
            if et < self.H_TIME:return False
            self.info[ip].begin_for_hours = time.time()
            self.info[ip].count_for_hours = 1
            self.info[ip].status = 0
            return True

        self.info[ip].count_for_day += 1
        self.info[ip].count_for_hours += 1

        if self.info[ip].count_for_day > self.D_MAX:
            if dt <= 24*3600:
                self.info[ip].status = 1
                self.info[ip].error_begin = time.time()
                return False
            self.info[ip].begin_for_day = time.time()
            self.info[ip].count_for_day = 1
            return True

        if self.info[ip].count_for_hours > self.H_MAX:
            if ht <= 3600:
                self.info[ip].status = 2
                self.info[ip].error_begin = time.time()
                return False
            self.info[ip].begin_for_hours = time.time()
            self.info[ip].count_for_hours = 1
            return True

        return True

global iptables
iptables = IpTables()

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        #print self.request.headers
        ip = self.request.remote_ip
        res = iptables.Check(ip)
        if res == False:
            self.send_error(503)
            return
        #print ip
        self.render('index.html')

class AboutUsHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        opt = pymongo.Connection('192.168.1.123')['SJLX_online']['City']
        citys = list()
        for city in opt.find():
            citys.append([city['city'],city['country']])
        self.render('about.html',code=open('./Blog.py','r').read(),code_type="brush: python;",citys=citys)

class Hello(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        logging.debug('hello')
        '''
        global total
        self.write(str(total))
        self.finish()
        total += 1
        '''
        #raise tornado.web.HTTPError(403)
        self.send_error(305)

class Search(tornado.web.RequestHandler):
    def post(self):
        #print self.request
        #print self.request.headers
        #print self.request.body
        #email = self.request.get_body_argument('email')
        #print email
        #print dir(self.request)
        #print self.request.query()
        #print self.request.query_arguments()
        #print self.get_argument('email')
        logging.debug(self.get_argument('email'))

'''
class Image(tornado.web.RequestHandler):
    def get(self):
        self.render('Image/test.jpg')
'''


def Server():
    settings = {}
    settings['cookie_secret'] = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
    settings['debug'] = True
    settings['template_path'] = os.path.join(os.path.dirname(__file__), "templates")
    settings['static_path'] = os.path.join(os.path.dirname(__file__), "static")
    server = tornado.web.Application(
        [
            (r'/',MainHandler),
            (r'/index',MainHandler),
            (r'/about',AboutUsHandler),
            (r'/hello',Hello),
            (r'/newsletter.php',Search),
        ],
        **settings
        #cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        #debug=True,
        #template_path=os.path.join(os.path.dirname(__file__), "templates"),
        #static_path=os.path.join(os.path.dirname(__file__), "static"),
        #image_path=os.path.join(os.path.dirname(__file__),"images")
    )
    server.listen(8887,'0.0.0.0')
    print 'start'
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    Server()
