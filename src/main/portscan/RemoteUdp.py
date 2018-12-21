#!/usr/bin/python
# -*- coding = UTF-8 -*-
import socket
import threading
import time
import struct
import Queue

queue = Queue.Queue()


def udp_sender(ip, port):
    try:
        addr = (ip, port)
        sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_udp.sendto("abcd...", addr)
        sock_udp.close()
    except socket.error:
        pass


def icmp_receiver(ip, port):
    icmp = socket.getprotobyname("icmp")
    try:
        sock_icmp = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    except socket.error, (errno, msg):
        if errno == 1:
            # Operation not permitted
            msg = msg + (
                " - Note that ICMP messages can only be sent from processes"
                " running as root."
            )
            raise socket.error(msg)
        raise  # raise the original error
    sock_icmp.settimeout(3)
    try:
        rec_packet, addr = sock_icmp.recvfrom(64)
    except socket.error:
        queue.put(True)
        return
    icmp_header = rec_packet[20:28]
    icmp_port = int(rec_packet.encode('hex')[100:104], 16)
    head_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", icmp_header)
    sock_icmp.close()
    if code == 3 and icmp_port == port and addr[0] == ip:
        queue.put(False)
    return


def checker_udp(ip, port):
    thread_udp = threading.Thread(target=udp_sender, args=(ip, port))
    thread_icmp = threading.Thread(target=icmp_receiver, args=(ip, port))
    thread_udp.daemon = True
    thread_icmp.daemon = True
    thread_icmp.start()
    time.sleep(0.1)
    thread_udp.start()
    thread_icmp.join()
    thread_udp.join()
    return queue.get(False)


if __name__ == '__main__':
    # print checker_udp(sys.argv[1], int(sys.argv[2]))
    print checker_udp("10.7.6.28", 123)
