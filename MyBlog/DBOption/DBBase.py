#coding=utf-8
import os
import re
import sys
import json
import bson
import uuid
import pymongo


class DBBase(object):
    commopt = pymongo.Connection('192.168.1.123')['SJLX_online']['CommentFilter']
    useropt = pymongo.Connection('192.168.1.123')['SJLX_online']['User']
