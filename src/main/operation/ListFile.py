#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import re
import os



# 列举当前目录以及所有子目录下的文件
print os.curdir
for root, dirs, files in os.walk('./'):
    for name in files:
        print (os.path.join(root, name))
