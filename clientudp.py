from socket import *
serverPort = 12000
serverName = 'bmsce-Precision-T1700'
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.connect((serverName,serverPort))
fileName = input("Enter file name: ")
clientSocket.sendto(bytes(fileName,'utf-8'),(serverName,serverPort))
content,serverAddr = clientSocket.recvfrom(2048)
print("File Contents: \n")
print(content.decode())
clientSocket.close()
