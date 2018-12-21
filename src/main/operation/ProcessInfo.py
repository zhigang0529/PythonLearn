#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psutil
import time
from operator import itemgetter


# 取出指定进程占用的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
def getProcessInfo(p):
    try:
        cpu = int(p.cpu_percent(interval=0))
        memory = p.memory_info()
        rss = memory.rss / 1024
        vms = memory.vms / 1024
        name = p.name()
        pid = p.pid
    except psutil.Error:
        name = "Closed_Process"
        pid = 0
        rss = 0
        vms = 0
        cpu = 0
    # return [name.upper(), pid, rss, vms]
    return [name, pid, vms, rss, cpu]


def getAllProcessInfo():
    """取出全部进程的进程名，进程ID，进程实际内存, 虚拟内存,CPU使用率
    """
    instances = []
    all_processes = list(psutil.process_iter())
    for proc in all_processes:
        proc.cpu_percent(interval=0)
        # 此处sleep1秒是取正确取出CPU使用率的重点
    time.sleep(1)
    for proc in all_processes:
        instances.append(getProcessInfo(proc))
    return instances


if __name__ == '__main__':
    processInfoList = getAllProcessInfo()
    processInfoList.sort(key=itemgetter(2), reverse=True)
    for p in processInfoList:
        print(p)
