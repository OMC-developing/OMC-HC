# -*- coding: utf-8 -*-
import socket

class Listener() :

    def __init__(self, port=6880):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # creating socket
        try:
            self.sock.bind(('', self.port))
        except OSError:
            print 'Port %s is busy!' % self.port


    def wait_connection(self):        
        self.sock.setblocking(1)
        self.sock.listen(0)

        self.conn, self.address = self.sock.accept()
        self.sock.close()

        try:
            self.conn.settimeout(60)
            print 'MC connected from %s' % self.address[0]
            while True:
                msg, status = self.receive()
                if status is False:
                    break
                
                print msg, status
                self.send('HC received message: %s' % msg)
                
        except Exception as e:
            print 'Exception: %s' % str(e)

            
    def receive(self):
        data = b''
        try:
            data += self.conn.recv(1024)

        except socket.timeout:
            print 'Socket timeout'
            return data, False

        except ConnectionResetError:
            print 'MC disconnected'
            return data, False            

        if not data:
            print 'MC closed session'
            return data, False
 
        return data, True


    def send(self, msg):
        print 'Send %s' %msg

        msg += '\r'
        try:
            self.conn.send(msg)
            return True
        except (ConnectionResetError, ConnectionAbortError):
            print 'MC disconnected before answer'
            return False
        
        except Exception as e:
            print 'Error to answer:', str(e) 
            return False


l = Listener()
l.wait_connection()
