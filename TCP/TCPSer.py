from socket import *
ADDR=('',60000)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpCliSock,addr=tcpSerSock.accept()
data=tcpCliSock.recv(1024)
print data
tcpCliSock.close()
tcpSerSock.close()
