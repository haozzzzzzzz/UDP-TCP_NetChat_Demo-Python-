from socket import *
ADDR=('localhost',60000)
tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    data=raw_input('>')
    tcpCliSock.send(data)
    data=tcpCliSock.recv(1024)
    print data
tcpCliSock.close()
