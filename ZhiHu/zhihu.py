#coding=utf-8
import os
import re
import sys
import json
import random
import urllib
import urllib2
import chardet
import requests
import gzip
from StringIO import StringIO

UA_LIST = [
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]

import cookielib
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)

def Post(url,data):
    request = urllib2.Request(url)
    request.add_header("User-Agent",random.choice(UA_LIST))
    request.add_header("Content-Type",'application/x-www-form-urlencoded; charset=UTF-8')
    request.add_header("Accept-Encoding",'gzip')
    request.add_header('Accept','*/*')
    request.add_header("Host","www.zhihu.com")
    request.add_header("Origin","http://www.zhihu.com")
    request.add_header("Referer","http://www.zhihu.com/topics")
    request.add_header("X-Requested-With","XMLHttpRequest")
    request.add_header("Pragma",'no-cache')
    request.add_header("Connection","keep-alive")
    request.add_header('Cache-Control','no-cache')
    data = urllib.urlencode(data)
    res = urllib2.urlopen(request,data)
    return res.read()

def Get(url):
    res = urllib2.urlopen(url)
    print res.code
    return res.read()

def TopicItemProcess(item):
    for res in re.finditer(r'<li data-id="(\d+)"><a href="(.*)">(.*)<\/a><\/li>',item):
        yield int(res.group(1)),res.group(3)

def TopicList():
    url = "http://www.zhihu.com/topics"
    data = Get(url)
    result = list()
    for res in TopicItemProcess(data):
        print res[0],res[1]
        result.append(list(res))
    json.dump(result,open('./topic_list.json','w'),ensure_ascii=False,indent=4)

def TopicsPlazzaListV2Process(item):
    pass

plazza = dict()

def TopicsPlazzaListV2(topic_id,offset = 0):
    url = 'http://www.zhihu.com/node/TopicsPlazzaListV2'
    msg = dict()
    msg['method'] = 'next'
    msg['params'] = {'topic_id':topic_id,'offset':offset,'hash_id':'307a71d97ae27c196a4e4184e81132a8'}
    msg['params'] = json.dumps(msg['params']).replace(" ",'')
    msg['_xsrf'] = '9f169055f3582408f934bf458443e635'
    res = Post(url,msg)
    print res
    result = StringIO(res)
    f = gzip.GzipFile(fileobj=result)
    result = f.read()
    res = json.loads(result)
    if res['r'] == 0:
        for item in res['msg']:
            res1 = re.search(r'<strong>(.+)<\/strong>',item)
            res2 = re.search(r'href="(\/topic\/\d+)">',item)
            title,url = res1.group(1).encode('utf-8'),res2.group(1)
            print title,url
            if url not in plazza:plazza[url] = [topic_id,title,url]
    return len(res['msg'])

def PlazzaList():
    data = json.load(open('./topic_list.json','r'))
    for topic in data:
        topic_id = topic[0]
        offset = 0
        while True:
            res = TopicsPlazzaListV2(topic_id,offset)
            if res == 0:break
            offset += res
        break
    #json.dump(plazza,open('./plazza_list.json','w'),ensure_ascii=False,indent=4)
if __name__ == '__main__':
    PlazzaList()
