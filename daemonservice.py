#!/usr/bin/env python
 
import sys, time
from daemonbase import Daemon

import socket
import threading

def handle_client(sock):
    with sock.makefile() as f:
        sock.close()
        for line in f:
            f.writeline(line)

def serve_forever():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind('', 12345)
    server.listen(1)
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client, args=[conn])
        thread.daemon = True
        thread.start()
 
class MyDaemon(Daemon):
    def run(self):
        while True:
            serve_forever()
            #with open('/tmp/daemon2', 'aw') as damn:
            #    damn.write('!')
            #time.sleep(10) 
 
if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)

