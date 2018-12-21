#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import psutil
import re
import os

'''
def cpu():
    print(psutil.cpu_stats())
    print(psutil.cpu_times())
cpu()


def disk():
    print(psutil.disk_io_counters())
    #print(psutil.disk_usage())
disk()
'''
'''
def write_netstat():
    print('[+]Write a port to a file')

querys = os.popen('netstat -an').read()
wsd = open('netstat.txt', 'w')
wsd.write(querys)
wsd.close()

write_netstat()
'''


def swsd():
    global usd, ow
    wsd = open('netstat.txt', 'r')
    swd = wsd.read()
    #print(swd)
    odf = re.findall(
        '(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d):(4012)',
        swd)
    usd = odf[0]
    print('[+]Query the IP address of a remote connection')
    df = usd[0], usd[1], usd[1], usd[3]
    wdst = ".".join(df)
    ow = wdst + ":" + usd[4]
    print(usd[0], '.', usd[1], '.', usd[2], '.', usd[3] + ":", usd[4])

swsd()
