#coding=utf-8
import os
import re
import sys
import json
import time
import pymongo
import datetime
import threading
import tornado
import IpSearch
#from DBOption import DBBase


class SystemInfo():
    user_info = list()
    comment_info = list()
    request_info = dict()
    commopt = pymongo.Connection('192.168.1.123')['SJLX_online']['CommentFilter']
    useropt = pymongo.Connection('192.168.1.123')['SJLX_online']['User']
    def Comment(self):
        print 'comment'
        start_time = datetime.datetime.now()+datetime.timedelta(days=-7)
        st = datetime.datetime.strftime(start_time,"%Y-%m-%D 00:00:00")
        self.comment_info = list()
        info = dict()
        for com in self.commopt.find({'mark':3,'datetime':{'$gte':st}},{'combin_id':1,'datetime':1}):
            combin_id = com['combin_id']
            dt = com['datetime']
            if dt not in info:
                info[dt] = dict()
                info[dt]['datetime'] = dt[:10]
                info[dt]['total'] = 0
                info[dt]['rest_ids'] = dict()
            info[dt]['total'] += 1
            #info[dt]['rest_ids'].add(combin_id)
            if combin_id not in info[dt]['rest_ids']:
                info[dt]['rest_ids'][combin_id] = 0
            info[dt]['rest_ids'][combin_id] += 1
        self.comment_info = sorted(info.values(),lambda A,B:cmp(A['datetime'],B['datetime']))

    def User(self):
        print 'user'
        start_time = datetime.datetime.now()+datetime.timedelta(days=-7)
        st = datetime.datetime.strftime(start_time,"%Y-%m-%d 00:00:00")
        self.user_info = list()
        info = dict()
        for user in self.useropt.find({'datetime':{'$gte':st},'new':1},{'regist_type':1,'datetime':1}):
            rt = user['regist_type']
            dt = user['datetime']
            if dt not in info:
                info[dt] = dict()
                info[dt]['datetime'] = dt[:10]
                info[dt]['total'] = 0
                info[dt]['regist_type'] = {'qq':0,'phone':0,'weibo':0,'mail':0}
            info[dt]['regist_type'][rt] += 1
            info[dt]['total'] += 1
        self.user_info = sorted(info.values(),lambda A,B:cmp(A['datetime'],B['datetime']))

    def Request(self):
        path = "/Users/yhrun/workspace/py_test/MyBlog/LogFile/"
        for d in os.listdir(path):
            p = path+d+'/'
            for f in os.listdir(p):
                if f != 'info.log':continue
                with open(p+f,'r') as file:
                    for line in file:
                        _date = line[1:11]
                        _datetime = line[1:20]
                        if _date != '2015-02-25':continue
                        line = line.strip()
                        line = line[line.find('{'):]
                        try:
                            msg = json.loads(line)
                            ip = msg['remote_ip']
                            if msg['url'] != '/restaurant/search.json':continue
                            result =  IpSearch.SinaAPI(ip)
                            if result['ret'] == -1:continue
                            if result['country'] == u'中国':continue
                            data = json.loads(msg['data'])
                            print data['region'],data['locality'],json.dumps(data['kind_lable'],ensure_ascii=False)
                            #print msg
                            #result =  IpSearch.SinaAPI(ip)
                            #if result['ret'] == -1:continue
                            #if result['country'] == u'中国':continue
                            #print datetime,ip,result['country']
                        except BaseException as e:
                            print e
    def start(self):
        self.Comment()
        self.User()
        self.Request()
        t = threading.Timer(24*3600,self.start)
        t.start()

global sysinfo
sysinfo = SystemInfo()
#tr = threading.Timer(10,sysinfo.start)
#tr.start()
sysinfo.Request()