import socket
from socket import*
serverPort = 15000
serverName = 'bmsce-Precision-T1700'
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print('the server is ready to recieve')
while 1:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    CapitalizedSentence = sentence.upper()
    connectionSocket.send( CapitalizedSentence.encode())
    connectionSocket.close()
    
