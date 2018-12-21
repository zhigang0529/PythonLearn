#!/usr/bin/python
# !coding=utf-8

import os

list = []
sum = 0
pslines = os.popen('ps aux', 'r').readlines()

for line in pslines:
    str2 = line.split()
    new_rss = str2[5]
    list.append(new_rss)

for i in list[1:-1]:
    num = int(i)
    sum = sum + num

print '%s:%s' % (list[0], sum)
