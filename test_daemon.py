# from https://stackoverflow.com/questions/15652791/how-to-create-a-python-socket-listner-deamon

import socket
import threading
import daemon

def handle_client(sock):
    with sock.makefile() as f:
        sock.close()
        for line in f:
            f.writeline(line)

def serve_forever():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 12345))
    server.listen(1)
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client, args=[conn])
        thread.daemon = True
        thread.start()

#with daemon.DaemonContext():
serve_forever()
