from socket import *
serverPort = 12000
serverName = 'bmsce-Precision-T1700'
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind((serverName,serverPort))
print('Ready')
while 1:
    fileName,addr = serverSocket.recvfrom(2048);
    file = open(fileName,"r")
    s = file.read(2048)
    serverSocket.sendto(s.encode(),addr)
    file.close()
