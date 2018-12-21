#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from datetime import datetime

datenow = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
logstr = "%s \n" % (datenow)
print logstr

# strftime 是将 datetime 转换为字符串，全称是 “string format time”
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print date_time + "\n"

# strptime 是将字符串转换为 datetime，全称是 “string parse time”
strptime = datetime.strptime('2018-10-15 20:59:29', '%Y-%m-%d %H:%M:%S')
print strptime
