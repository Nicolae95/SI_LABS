import sys
import socket


def udp_send(dt, data):
    HOST, PORT = "localhost", 9090
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(dt + "," + data + "\n")
        received = sock.recv(1024)
    finally:
        sock.close()
    print "Sent:     %s"%data
    print "Received: %s"%received


def tcp_send(dt, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 9000))
    sock.sendall(dt + "," + data)
    received = sock.recv(1024)
    print "Sent:     %s"%data
    print "Received: %s"%received
    sock.close()



if __name__ == "__main__":
    mtype = sys.argv[1]
    mess = sys.argv[2]
    data = sys.argv[3]

    print(mtype, mess, data)

    if mtype == '-u':
        udp_send(mess, data)
    elif mtype == '-t':
        tcp_send(mess, data)
