#!/usr/bin/env python
# coding-utf
import argparse
import socket
import sys


def scan_ports(host, start_port, end_port):
    """Scan remote hosts"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
    except socket.error, error_msg:
        print 'Socket creation failed.Error code:' + str(error_msg[0]) + 'Erroe message:' + error_msg[0]
        sys.exit()
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.error, error_msg:
        print error_msg
        sys.exit()
    # end_port +=
    for port in range(start_port, end_port):
        try:
            sock.connect((remote_ip, port))
            print 'Port ' + str(port) + ' is open'
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, error_msg:
            # print(str(port), ' error ' , error_msg)
            pass


if __name__ == '__main__':
    scan_ports("czg", 100, 1000)
    '''
    parser = argparse.ArgumentParser(description='remote port scaner')
    parser.add_argument('--host', action="store", dest="host", default='www.wealink.com')
    parser.add_argument('--start-port', action="store", dest="start_port", default='', type = int)
    parser.add_argument('--end-port', action="store", dest="end_port", default='', type = int)
    given_args = parser.parse_args()
    host, start_port, end_start = given_args.host, given_args.start_port, given_args.end_port
    scan_ports(host, start_port, end_start)
'''