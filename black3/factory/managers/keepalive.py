# coding=utf-8

import threading
import time
import urllib2
import os
import sys
from factory.supports.singletonmaker import singleton
from rootcfg import KEEPALIVE_URL_PREFIX

"""
worker:
    weibo:"busy"
"""


@singleton
class keepalive(threading.Thread):
    def __init__(self, name, inteval):
        self.name = name
        self.url = KEEPALIVE_URL_PREFIX + name
        self.thread_stop = False
        self.inteval = inteval


    def run(self):
        while (not self.thread_stop):
            self.send_heartbeat()
            print time.ctime() + ": send a heatbeat to scheduler"
            time.sleep(self.inteval)


    def kill(self):
        self.thread_stop = True


    #worker needs a feedback?
    def send_heartbeat(self):
        data = {
            "mem": "1024",
            "usage": "512"
        }
        req = urllib2.Request(self.url, data=data)
        req.get_method = lambda: 'PUT'
        response = urllib2.urlopen(req)