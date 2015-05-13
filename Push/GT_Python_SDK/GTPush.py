# -*- coding: utf-8 -*-
__author__ = 'wei'
#更新时间为2013年11月07日
#增加了IOS的离线消息推送,IOS不支持IGtNotyPopLoadTemplate模板
#更新时间为2013年02月24日
#1.增加了通知弹框下载模板 
#2.统一了toapp的接口时间，单位为毫秒 
#3.允许ios用户离线状态下的apn转发message字段为空，
#4.增加了查询用户状态接口，
#5.任务停止功能，
#6.增加ToList接口每个用户返回用户状态的功能
#更新时间为2014年08月30日
#1.IOS在设置setPushInfo为{"",-1,"","","","","",""} 会抛出异常，不允许设置
#更新时间为2014年09月10日
#1.增加APN简化版推送功能，推送接口apnPush()
#    a.注册应用后，不需集成SDK（IOS）版本
#    b.可根据IOS的DeivceToken推送APN消息
#更新时间为2014年10月29日
#1.增加任务组名自定义功能，组名可为中英文，数字，下划线

from igt_push import *
from igetui.template import *
from igetui.template.igt_base_template import *
from igetui.template.igt_transmission_template import *
from igetui.template.igt_link_template import *
from igetui.template.igt_notification_template import *
from igetui.template.igt_notypopload_template import *
from igetui.template.igt_apn_template import *
from igetui.igt_message import *
from igetui.igt_target import *
from igetui.template import *
import uuid
import datetime
import time

#toList接口每个用户返回用户状态开关,true：打开 false：关闭
os.environ['needDetails'] = 'true'
APPID = "QoZV0s9bAs6ehHm3wm6Vh3"
APPKEY = "VRL1U2NQom6APUE0pKzQw3"
MASTERSECRET = "G9Fb6M3II58d7vpD1iBEw1"
CID = ""
HOST = 'http://sdk.open.api.igexin.com/apiex.htm'
DEVICETOKEN = ""

def pushAPN():

    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    message = IGtSingleMessage()
    template = APNTemplate()
    template.setPushInfo("", 1,'近10场8胜2负的开拓者状', "", '{"k":"p","v":{"vi":362,"vn":"BTV","pt":1},"mid":2583}', "", "", "",1)
    #单个用户推送接口
    message.data = template
    ret = push.pushAPNMessageToSingle(APPID, DEVICETOKEN, message)
    print ret

    #多个用户推送接口
    #message = IGtListMessage()
    #message.data = template
    #contentId = push.getAPNContentId(APPID, message)
    #deviceTokenList = []
    #deviceTokenList.append(DEVICETOKEN)
    #ret = push.pushAPNMessageToList(APPID, contentId, deviceTokenList)
    #print ret

def pushMessageToSingle():
    time_start = time.time()
    push = IGeTui(HOST,APPKEY, MASTERSECRET)
    time_end = time.time()
    print "user check time:",str(time_end-time_start)
    print push
    #消息模版：
    #1.TransmissionTemplate:透传功能模板
    #2.LinkTemplate:通知打开链接功能模板
    #3.NotificationTemplate：通知透传功能模板
    #4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    #template = LinkTemplateDemo()
    #template = TransmissionTemplateDemo()
    #template = NotyPopLoadTemplateDemo()
	
    message = IGtSingleMessage()
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.data = template
    #message.pushNetWorkType = 2

    target = Target()
    target.appId = APPID
    target.clientId = CID

    ret = push.pushMessageToSingle(message, target)
    print ret


def pushMessageToList():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)

    #消息模版： 
    #1.TransmissionTemplate:透传功能模板  
    #2.LinkTemplate:通知打开链接功能模板  
    #3.NotificationTemplate：通知透传功能模板  
    #4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    #template = LinkTemplateDemo()
    #template = TransmissionTemplateDemo()
    #template = NotyPopLoadTemplateDemo()

    message = IGtListMessage()
    message.data = template
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.pushNetWorkType = 0

    target1 = Target()
    target1.appId = APPID
    target1.clientId = CID

    #target2 = Target()
    #target2.appId = APPID
    #target2.clientId = CID

    targets = [target1]
    contentId = push.getContentId(message,'ToList_任务别名_可为空')
    ret = push.pushMessageToList(contentId, targets)
    print ret


def pushMessageToApp():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)

    #消息模版： 
    #1.TransmissionTemplate:透传功能模板  
    #2.LinkTemplate:通知打开链接功能模板  
    #3.NotificationTemplate：通知透传功能模板  
    #4.NotyPopLoadTemplate：通知弹框下载功能模板

    template = NotificationTemplateDemo()
    #template = LinkTemplateDemo()
    #template = TransmissionTemplateDemo()
    #template = NotyPopLoadTemplateDemo()

    message = IGtAppMessage()
    message.data = template
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.appIdList.extend([APPID])
    #message.phoneTypeList.extend(["ANDROID", "IOS"])
    #message.provinceList.extend(["浙江", "上海"])
    #message.tagList.extend(["开心"])
    #message.pushNetWorkType = 1
    message.setSpeed(10)
    ret = push.pushMessageToApp(message)
    #print message.getSpeed()
    print ret

def SendMessage(data):

    time_start = time.time()
    push = IGeTui(HOST,APPKEY, MASTERSECRET)
    time_end = time.time()
    print "user check time:",str(time_end-time_start)

    tmp = TransmissionTemplate()
    tmp.appId = APPID
    tmp.appKey = APPKEY
    tmp.transmissionContent = json.dumps(data)
    tmp.transmissionType = 2
    message = IGtAppMessage()
    message.data = tmp
    message.isOffline = True
    message.offlineExpireTime = 1000 * 3600 * 12
    message.appIdList.extend([APPID])
    #message.phoneTypeList.extend(["ANDROID", "IOS"])
    #message.provinceList.extend(["浙江", "上海"])
    #message.tagList.extend(["开心"])
    #message.pushNetWorkType = 1
    message.setSpeed(10)
    ret = push.pushMessageToApp(message)
    print ret

#通知透传模板动作内容
def NotificationTemplateDemo():
    template = NotificationTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionType = 1
    template.transmissionContent = u"请填入透传内容"
    template.title = u"请填入通知标题"
    template.text = u"请填入通知内容"
    template.logo = "icon.png"
    template.logoURL = ""
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    #iOS 推送需要的PushInfo字段 前三项必填，后四项可以填空字符串
    #template.setPushInfo(actionLocKey, badge, message, sound, payload, locKey, locArgs, launchImage)
    #template.setPushInfo("open",4,"message","","","","","");
    begin = "2015-03-04 17:40:22";
    end = "2015-04-21 17:47:24";
    template.setDuration(begin, end)
    return template

#通知链接模板动作内容
def LinkTemplateDemo():
    template = LinkTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.title = u"请填入通知标题"
    template.text = u"请填入通知内容"
    template.logo = ""
    template.url = "http://www.baidu.com"
    template.transmissionType = 1
    template.transmissionContent = ''
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
    #iOS 推送需要的PushInfo字段 前三项必填，后四项可以填空字符串
    #template.setPushInfo(actionLocKey, badge, message, sound, payload, locKey, locArgs, launchImage)
    #template.setPushInfo("open",4,"message","test1.wav","","","","");
    return template

#透传模板动作内容
def TransmissionTemplateDemo():
    template = TransmissionTemplate()
    template.transmissionType = 1
    template.appId = APPID
    template.appKey = APPKEY
    template.transmissionContent = '请填入透传内容'
    #iOS 推送需要的PushInfo字段 前三项必填，后四项可以填空字符串
    #template.setPushInfo(actionLocKey, badge, message, sound, payload, locKey, locArgs, launchImage)
    template.setPushInfo("",0,"","com.gexin.ios.silence","","","","");
    
    return template

#通知弹框下载模板动作内容
def NotyPopLoadTemplateDemo():
    template = NotyPopLoadTemplate()
    template.appId = APPID
    template.appKey = APPKEY
    template.notyIcon = "icon.png"
    template.logoUrl = ""
    template.notyTitle = u"通知弹框下载功能标题"
    template.notyContent= u"通知弹框下载功能内容"
    template.isRing = True
    template.isVibrate = True
    template.isClearable = True
	
    template.popTitle = u"弹框标题"
    template.popContent = u"弹框内容"
    template.popImage = ""
    template.popButton1 = u"下载"
    template.popButton2 = u"取消"

    template.loadIcon = "file://icon.png"
    template.loadTitle = u"下载内容"
    template.loadUrl = "http://gdown.baidu.com/data/wisegame/c95836e06c224f51/weixinxinqing_5.apk"
    template.isAutoInstall = True
    template.isActive = False
    return template

#获取用户状态
def getUserStatus():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    print push.getClientIdStatus(APPID, CID)

#任务停止功能
def stopTask():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    print push.stop("OSA-0226_50RYYPFmos9eQEHZrkAf27");	
 
#根据ClientID设置标签功能
def setTag():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    tagList =['标签1','标签2','......']
    print push.setClientTag(APPID,CID,tagList);

#根据taskId返回推送结果
def getPushResultTest():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    print push.getPushResult("OSA-0420_YRQxGVe82GAKU43BfkfmB6")

#根据ClientID查询标签
def getUserTagsTest():
    push = IGeTui(HOST, APPKEY, MASTERSECRET)
    dictz= push.getUserTags(APPID,CID)
    for key in dictz:
	print key+":"+dictz[key].decode("utf-8")        

    #
    #服务端支持三个接口推送
    #1.PushMessageToSingle接口：支持对单个用户进行推送
    #2.PushMessageToList接口：支持对多个用户进行推送，建议为50个用户
    #3.pushMessageToApp接口：对单个应用下的所有用户进行推送，可根据省份，标签，机型过滤推送
    #



if __name__ == '__main__':
    #pushMessageToSingle()
    #getUserTagsTest()
    #pushMessageToApp()
    #getPushResultTest()
    #getUserStatus()
    msg = {'type':'image','title':'','content':'发送一条消息','image':""}
    user_info = {'user_id':'qq_BBE55A0E75D0746F82F49731FF312111','user_name':'宋富成Xml','head_image':"http://q.qlogo.cn/qqapp/1102902925/BBE55A0E75D0746F82F49731FF312111/100"}
    #Push(u'今天天气不错')

    message = dict()
    message['mine'] = False
    message['type'] = "message"
    message['message_id'] = str(uuid.uuid1()).replace('-','')
    message['datetime'] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
    message['look_over'] = False
    message['message'] = msg
    message['user_info'] = user_info

    data = {'type':'message','message':msg,'user_info':user_info}
    SendMessage(message)
