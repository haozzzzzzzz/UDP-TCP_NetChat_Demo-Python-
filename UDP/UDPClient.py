from socket import *
ADDR=('localhost',60000)
udpCliSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=raw_input('>')
    udpCliSock.sendto(data,ADDR)
    data,addr=udpCliSock.recvfrom(1024)
    print data
udpCliSock.close()
