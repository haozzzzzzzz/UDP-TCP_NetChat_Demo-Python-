from socket import *

ADDR=('',60000)
udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)
while True:
    data,addr=udpSerSock.recvfrom(1024)
    print data
    data=raw_input('>')
    udpSerSock.sendto(data,addr)
udpSerSock.close()
