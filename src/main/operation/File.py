#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import psutil
from io import open

file_path = "content.txt"

# 写文件内容
content = u'''Python is a programming language that lets you work quickly
and integrate systems more effectively.'''
f1 = open(file_path, "a")  # a是追加文件内容
f1.write(content)
f1.write(u"\n")
f1.close()

'''
#读文件内容
f2 = open(file_path, 'r')
#不带参数的read()函数一次读入文件的所有内容
print(f2.read())
f2.close()
'''
'''
#将数据进行分块，直到所有字符被写入
fout = open(file_path, "w")
size = len(content)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(content[offset:offset+chunk])
    offset += chunk
fout.close()
'''
'''
#readline()每次读入文件的一行，通过追加每一行拼接成原来的字符串：
ct = ""
fin = open(file_path, "r")
while True:
    line = fin.readline()
    if not line:
        break
    ct += line
fin.close()
print(ct)
'''

'''
# 函数readlines()调用时每次读取一行，并返回单行字符串的列表
f3 = open(file_path, "r")
lines = f3.readlines()
f3.close()
for line in lines:
    print(line)  # print(line, end="")
'''

print("Writer number to file")
f4 = open("number.txt", "w+")
for i in range(10):
    f4.write(u'write ' + str(i) + '\n')
f4.flush()
f4.close()