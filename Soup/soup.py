#coding=utf-8
import os
import re
import sys
import json
import urllib
import random
import urllib2
import HTMLParser
from BeautifulSoup import BeautifulSoup

UA_LIST = [
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]

html_parser = HTMLParser.HTMLParser()

def GET(url):
    request = urllib2.Request(url)
    request.add_header('User-agent',random.choice(UA_LIST))
    response = urllib2.urlopen(request,timeout=30)
    return response.read()

class RestParse(object):
    def __init__(self,soup):
        self.soup = soup

    def RestName(self):
        title = self.soup.find('div',{'class':'dest_toptitle detail_tt'})
        print 'title(zh) : ',title.h1.text
        if title.p != None:
            print 'title(local) : ',html_parser.unescape(title.p.text).split('\n')[0]

    def DetailTop_r_info(self):
        detailtop_r_info = self.soup.find('ul',{'class':'detailtop_r_info'})
        score = detailtop_r_info.find('span',{'class':'score'})
        if score != None:
            print '评分 : ',score.b.text
        comment_count = detailtop_r_info.find('span',{'class':'f_orange'})
        if comment_count != None:
            print '评论 : ',comment_count.text

    def RestDetail(self):
        box = self.soup.find('div',{'class':'normalbox'})
        info = box.find('div',{'class':'detailcon'})
        #desc = info.find('div',{'class':'text_style','itemprop':'description'})
        #if desc != None:print '描述 : ',desc.text
        for item in info.findAll('div',recursive=False):
            #print type(item)
            if item.has_key('itemprop'):
                print '描述 : ',item.text
            elif item['class'] == 'text_style':
                print '本店特色美食 : ',item.p.text
            elif item.h2 != None:
                h2 = item.h2.text
                if h2 == u'交通':
                    print '交通 : ',item.div.text
                elif h2 == u'特别提示':print '特别提示 : ',item.div.text
        #print div.next_elements
    def RestInfo(self):
        s_sight_infor = self.soup.find('div',{'class':'s_sight_infor'})
        base = s_sight_infor.find('ul',{'class':'s_sight_in_list s_sight_noline cf'})
        for item in base.findAll('li'):
            key = item.span.text

            if key == u'人 均：':
                print '人均 : ',html_parser.unescape(item.find('span',{'class':'s_sight_con'}).text)
            elif key == u'菜 系：':
                print '菜系 : ',
                for dish in item.findAll('a'):print dish.text,'  ',
                print
            elif key == u'电 话：':
                print '电话 : ',html_parser.unescape(item.find('span',{'class':'s_sight_con'}).text)

            elif key == u'地 址：':
                print '地址 : ',html_parser.unescape(item.find('span',{'class':'s_sight_con'}).text)

            elif key == u'营业时间：':
                print '营业时间 : ',html_parser.unescape(item.find('span',{'class':'s_sight_con'}).text)

    def Other(self):
        latitude = self.soup.find('input',{'id':'Lat'})
        print 'latitude : ',latitude['value']
        longitude = self.soup.find('input',{'id':'Lon'})
        print 'longitude : ',longitude['value']
        poiid = self.soup.find('input',{'id':'POIID'})
        print 'poiid : ',poiid['value']
        districtid = self.soup.find('input',{'id':'JS_DistrictId'})
        print 'districtid : ',districtid['value']


def Soup(data=None):
    url = 'http://you.ctrip.com/food/tokyo294/500233.html'
    #url = 'http://you.ctrip.com/food/tokyo294/9390866.html'
    if data == None:
        data = GET(url)
    soup = BeautifulSoup(data)
    rest = RestParse(soup)
    rest.RestName()
    rest.DetailTop_r_info()
    rest.RestDetail()
    rest.RestInfo()
    rest.Other()

def Image():
    url = 'http://you.ctrip.com/DestinationSite/TTDSecond/Photo/AjaxPhotoList?p=1&type=3&resource=500233&districtId=294'
    data = GET(url)
    soup = BeautifulSoup(data)
    for img in soup.findAll('img'):
        print img['src'],img['alt']

if __name__ == '__main__':
    
    path = '/Users/yhrun/workspace/MyEnv/workspace/CTRIP/data/Rest/RestDetail/'
    for file_name in os.listdir(path):
        data = open(path+file_name,'r').read()
        Soup(data)
    
    #Soup()
    #Image()
