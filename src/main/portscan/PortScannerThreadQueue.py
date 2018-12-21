#!/usr/bin/python
# _*_ coding = UTF-8 _*_

import socket
import threading
from Queue import Queue

'''
#加queue,变成生产者-消费者模式,开固定线程
'''
def scan(port):
    sk = socket.socket()
    sk.settimeout(0.1)
    if sk.connect_ex(('localhost', port)) == 0:
        print port, 'open'
        sk.close()


def worker():
    while not q.empty():
        port = q.get()
        try:
            scan(port)
        finally:
            q.task_done()


if __name__ == '__main__':
    q = Queue()
    map(q.put, xrange(1, 65535))
    threads = [threading.Thread(target=worker) for i in xrange(500)]
    map(lambda x: x.start(), threads)
    q.join()
