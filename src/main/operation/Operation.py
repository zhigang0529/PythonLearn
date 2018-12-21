#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import os
from io import open


def netstat():
    print("netstat -an")
    querys = os.popen('netstat -an').read()
    # print(querys)
    f = os.open("netstat.txt", os.O_CREAT | os.O_RDWR)
    n = os.write(f, querys)

netstat()

f = open("netstat.txt", "r")
for line in f.readlines():
    print(line)
f.close()