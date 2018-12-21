#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import socket
import threading
import time

service = ['mixcztdb.erp3.crland.com.cn 1526', 'ztcommon.crland.cn 8081',
           'ztshop.crland.cn 80', 'opera.crland.com.cn 80',
           'opera.crland.cn 80', 'invest.saas.crland.com.cn 80',
           'zt_rediscol1.erp3.crland.com.cn 7001', 'zt_rediscol1.erp3.crland.com.cn 7002',
           'zt_rediscol2.erp3.crland.com.cn 7001', 'zt_rediscol2.erp3.crland.com.cn 7002',
           'zt_rediscol3.erp3.crland.com.cn 7001', 'zt_rediscol3.erp3.crland.com.cn 7002']


def socketconnect(addr, port):
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(2)
        sk.connect((addr, int(port)))
        # print 'connect to ' + addr + ' ' + port + ' success'
    except socket.error, e:
        print 'connect to ' + addr + ' ' + port + ' timed out'
    sk.close()


def check():
    for every in service:
        addr = every.split()
        socketconnect(addr[0], addr[1])


if __name__ == '__main__':
    threads = [threading.Thread(target=check())]
    map(lambda x: x.start(), threads)
