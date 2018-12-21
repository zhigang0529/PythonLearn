# /usr/bin/python
# coding:utf-8
import os, sys
import re
from pprint import pprint

MIB = {
    'public': {
        'ports': {
            'string': '.1.3.6.1.2.1.2.2.1.2',
            'status': '.1.3.6.1.2.1.2.2.1.8',  # 2 down
        }
    },
    'huawei': {
    },
    'cisco': {
    }
}


def portStatus(_s):
    if int(_s) == 2:
        return 'down'
    elif int(_s) == 1:
        return 'up'
    else:
        return 'none'


#
def snmpwalk(host, publicKey, iso):
    return [i.strip() for i in os.popen('/usr/bin/snmpwalk -c %s  -v 2c %s %s' % (publicKey, host, iso)).readlines()]


def getPorts(_ip, _public, option):
    if option == 'ports':
        postsstring = (j.split('=')[1].split(':')[1].replace('"', '').strip() for j in
                       snmpwalk(_ip, _public, MIB['public']['ports']['string']))
        postsstatus = (int(j.split('=')[1].split(':')[1].strip()) for j in
                       snmpwalk(_ip, _public, MIB['public']['ports']['status']))
        return zip(postsstring, postsstatus)
    else:
        print('on this commmnad')


publicKey = 'hi'  # sunmp public key
HOSTS = {
    '10.221.98.2': {'type': 'switch', 'origin': 'quidway', 'public': publicKey},
    '10.221.98.3': {'type': 'switch', 'origin': 'quidway', 'public': publicKey},
    '10.221.97.108': {'type': 'firewall', 'origin': 'h3c', 'public': publicKey},
    '10.231.98.233': {'type': 'switch', 'origin': 'cisco', 'public': publicKey},
}


if __name__ == '__main__':
    for i in HOSTS.keys():
        for host, status in getPorts(i, HOSTS[i]['public'], 'ports'):
            print("%s\t%s\t%s" % (i, host.ljust(30), portStatus(status).ljust(20)))
        print(''.ljust(50, '#'))
