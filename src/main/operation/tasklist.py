#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import os


def tasklist():
    mem_size = 0.0
    service_count = 0
    task_list = os.popen("tasklist").readlines()
    try:
        for line in task_list:
            mem = line.split()
            if len(mem) != 0:
                if mem[0] == 'System Idle':
                    continue
                service_count += 1
                if len(mem[4]) != 0:
                    size = mem[4].replace(',', '')
                    if size.isdigit():
                        mem_size += int(size)
        size_mb = mem_size / 1024
    except ArithmeticError:
        print "Error: 没有找到文件或读取文件失败"
    else:
        print "成功"
    print("Memory size: %s MB" % size_mb)
    print("Service count: %s" % service_count)


tasklist()
