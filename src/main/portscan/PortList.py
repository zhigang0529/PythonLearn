from threading import Thread, activeCount
import socket
import os


def test_port(dst, port):
    os.system('title ' + str(port))
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        indicator = cli_sock.connect_ex((dst, port))
        if indicator == 0:
            print(port)
    except socket.error:
        print 'connect ' + dst + ' ' + port + ' error'
    finally:
        cli_sock.close()


if __name__ == '__main__':
    dst = '127.0.0.1'

    i = 0
    while i < 65536:
        # Return the number of Thread objects currently alive.
        if activeCount() <= 200:
            Thread(target=test_port, args=(dst, i)).start()
            i = i + 1

    while True:
        if activeCount() == 2:
            break

    input('Finished scanning.')
