from socket import *
ADDR=('localhost',60000)
tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
data=raw_input('>')
tcpCliSock.send(data)
tcpCliSock.close()
