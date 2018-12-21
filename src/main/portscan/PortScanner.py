#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import socket
import threading


def scan(port):
    s = socket.socket()
    s.settimeout(0.1)
    if s.connect_ex(('localhost', port)) == 0:
        print port, 'open'
    s.close()

"""
if __name__ == '__main__':
    threads = [threading.Thread(target=scan, args=(i,)) for i in xrange(1, 65536)]
    map(lambda x: x.start(), threads)
"""


# 判断远程端口是否打开
def remote(addr, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((addr, port))       # Tuple
        print 'Server ' + addr + ' port ' + str(port) + ' OK!'
    except Exception:
        print 'Server ' + addr + ' port ' + str(port) + ' not connect!'
    sk.close()

remote("localhost", 80)
