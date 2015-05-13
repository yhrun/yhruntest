#coding=utf-8
import os
import re
import sys
import json
import urllib
import urllib2


def Request(ip):
    url = "http://www.ip138.com/ips1388.asp?ip="+ip+"&action=2"
    #print url
    try:
        msg = urllib2.urlopen(url)
        data = msg.read()
        data = data.decode('gbk').encode('utf-8')
        res = re.search(r'<td align="center"><ul class="ul1"><li>(.*)<\/li><li>',data)
        if res == None:return ""
        city = res.group(1).replace("本站主数据：","")
        #print city
        return city
    except:
        return ""

def SinaAPI(ip):
    url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip="+ip
    res = urllib2.urlopen(url)
    data = res.read()
    data = data[:-1]
    data = data.replace('var remote_ip_info = ','')
    msg = json.loads(data)
    return msg


if __name__ == '__main__':
    #Request("182.92.71.179")
    SinaAPI('114.32.2.91')
    '''
    dir = "/Users/yhrun/workspace/Dingding/Log/"
    ips = dict()
    for p in os.listdir(dir):
        file = dir+p
        for f in os.listdir(file):
            _file = file+"/"+f
            with open(_file,'r') as filedata:
                for line in filedata:
                    line = line.strip()[line.find('{'):]
                    msg = json.loads(line)
                    if 'remote_ip' in msg:
                        ip = msg['remote_ip'].strip()
                        if ip not in ips:ips[ip] = 0
                        ips[ip] += 1

    print len(ips)
    info = dict()
    for ip,count in ips.iteritems():
        res = Request(ip)
        if res == "":continue
        city = res.split()[0]
        if city not in info:info[city] = 0
        info[city] += count
        print city,info[city]
        ips[ip] = [ip,count,city]
    json.dump(ips,open('./ipinfo.json','w'),ensure_ascii=False,indent=4)
    '''
