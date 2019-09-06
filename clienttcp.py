from socket import*
serverPort = 15000
serverName = 'bmsce-Precision-T1700'
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("enter sentence")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('from Server:',modifiedSentence.decode())
clientSocket.close()from socket import*
serverPort = 15000
serverName = 'bmsce-Precision-T1700'
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("enter sentence")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('from Server:',modifiedSentence.decode())
clientSocket.close()from socket import*
serverPort = 15000
serverName = 'bmsce-Precision-T1700'
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("enter sentence")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('from Server:',modifiedSentence.decode())
clientSocket.close()
