from threading import Thread
import socket

counting_open = []
counting_close = []
threads = []

def scan(port, host):
    s = socket.socket()
    targetIP = socket.gethostbyname(host)
    result = s.connect_ex((targetIP,port))
    # print('working on port > '+(str(port)))      
    if result == 0:
    	counting_open.append(port)
    	#print((str(port))+' -> open') 
    	s.close()
    else:
    	counting_close.append(port)
    	#print((str(port))+' -> close') 
    	s.close()

def scanner(host, from_port, to_port):
    for i in range(from_port, to_port+1):
    	t = Thread(target=scan, args=(i, host))
	threads.append(t)
	t.start()
	
    [x.join() for x in threads]

    print counting_open