from socket import *
ADDR=('',60000)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    tcpCliSock,addr=tcpSerSock.accept()
    while True:
        data=tcpCliSock.recv(1024)
        print data
        data=raw_input('>')
        tcpCliSock.send(data)
    tcpCliSock.close()
tcpSerSock.close()
