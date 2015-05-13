#coding=utf-8
import os
import re
import sys
import json
import time
import urllib
from Logging import Logging
import logging
import tornado
from tornado import web
from tornado import options
from tornado.options import define,options
import tornado.testing
global total
total = 1
class Test(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        '''
        if not self.get_secure_cookie('mycookie'):
            self.set_secure_cookie("mycookie", "myvalue")
            self.write("Your cookie was not set yet!")
            self.finish()
            return
        '''
        #items = ["Item 1", "Item 2", "Item 3"]
        #self.render("hello.html", title={'name':'test'}, items=items,sent="test")
        #raise ValueError
        self.render('index.html')
        #raise tornado.web.HTTPError(404)

        #self.write('hello')
        #time.sleep(10)
        #self.write('wake')
        #self.finish()

    def get_error_html(self, status_code, exception=None, **kwargs):
        print status_code
        #print exception
        #print kwargs
        raise tornado.web.HTTPError(404)
        pass

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
    server = tornado.web.Application(
        [
            (r'/test',Test),
            (r'/hello',Hello),
            (r'/newsletter.php',Search),
        ],
        cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
        debug=True,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        #image_path=os.path.join(os.path.dirname(__file__),"images")
    )
    server.listen(8887,'0.0.0.0')
    print 'start'
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    Server()
