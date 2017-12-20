#!/usr/bin/python
import threading
import SocketServer
import requests

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request[0].strip()
        port = self.client_address[1]
        socket = self.request[1]
        client_address = (self.client_address[0])
        cur_thread = threading.current_thread()
        print "thread %s" %cur_thread.name
        print "received call from client address :%s" %client_address
        print "received data from port [%s]: %s" %(port,data)
		### assemble a response message to client
        response = "%s %s"%(cur_thread.name, data)
        data = data.split(",")
        if data[0] == '-get':
            rq = requests.get(data[1])
            rq = str(rq.text.encode('utf-8'))
            socket.sendto(rq, self.client_address)
        else:
            socket.sendto(data[1], self.client_address)

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9090

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)
    ip, port = server.server_address
    server.serve_forever()
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    server.shutdown()