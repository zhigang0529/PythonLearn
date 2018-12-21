#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
import paramiko
import os


# 查询所有主机硬盘空间大小
def sshclientrsakey(ipaddr):
    private_key_path = '/root/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(private_key_path)

    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ipaddr, port=22, username='root', pkey=key, timeout=10)
    stdin, stdout, stderr = ssh.exec_command('df')
    print stdout.read()
    ssh.close()


# 查询所有主机硬盘空间大小
def sshclient(ipaddr):
    # 创建SSH对象
    ssh = paramiko.SSHClient()

    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 连接服务器
    ssh.connect(hostname='centos', port=22, username='root', password='123456')

    stdin, stdout, stderr = ssh.exec_command('df')
    print stdout.read()
    ssh.close()


def ping(ip):
    rs = os.system("ping " + ip).readline()
    print str(rs)


if __name__ == '__main__':
    # ping("127.0.0.1")
    ip_list = ['192.168.237.131', '127.0.0.1']

    for i in ip_list:
        p = Process(target=sshclient, args=(i,))
        p.start()
