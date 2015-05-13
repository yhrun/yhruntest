#coding=utf-8
import os
import sys
import json
import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()

def Info():
    url = "https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2015-02-23&leftTicketDTO.from_station=XUN&leftTicketDTO.to_station=BJP&purpose_codes=ADULT"
    handler=urllib2.HTTPCookieProcessor(cookie)
    opener=urllib2.build_opener(handler)
    res = opener.open(url)
    
    data = res.read()
    print data
    data = json.loads(data)
    for train in data['data']:
        train = train['queryLeftNewDTO']
        if train['canWebBuy'] == 'N':continue
        print train['station_train_code'],train['from_station_name'],'------->',train['to_station_name'],':',train['start_time']
        print 
        print '硬卧  二等座  硬座'
        print train['yw_num'],'   ',train['ze_num'],'   ',train['yz_num']
        print

def CodeCheck(code):
    url = 'https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn'
    msg = dict()
    msg['randCode'] = code
    msg['rand'] = 'sjrand'
    msg['randCode_validate'] = ''
    res = urllib2.urlopen(url,urllib.urlencode(msg))
    print res.code
    print res.read()
def GetCode():
    url = 'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&0.7950622919015586'
    res = urllib2.urlopen(url)
    print res.code
    data = res.read()
    open('./code.jpg','w').write(data)


def CityList():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.827'
    res = urllib2.urlopen(url)
    data = res.read()
    citys = list()
    ss = data.split('@')
    for city in ss:
        if city.find('|') == -1:continue
        msg = city.split('|')
        citys.append([msg[1].strip(),msg[2].strip()])
    json.dump(citys,open('./citylist.json','w'),ensure_ascii=False,indent=4)

def Login():
    GetCode()
    print 'code get success'
    msg = dict()
    url = 'https://kyfw.12306.cn/otn/login/loginAysnSuggest'
    msg['loginUserDTO.user_name'] = 'yhruner'
    msg['userDTO.password'] = 'yehao09.07'
    msg['randCode_validate'] = ''
    msg['MjEzMjg4'] = 'M2ViODc1ZTY5Y2RiZjQyNw=='
    msg['myversion'] = 'undefined'
    msg['randCode'] = raw_input().strip()
    print 'check code'
    CodeCheck(msg['randCode'])
    print 'end'
    print json.dumps(msg,indent=4)
    res = urllib2.urlopen(url,urllib.urlencode(msg))
    print res.code
    data = res.read()
    print data
        
if __name__ == '__main__':
    #CityList()
    #GetCode()
    #Login()
    Info()
