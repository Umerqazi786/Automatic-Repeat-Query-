import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host, port))
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.listen(5)
print ('Sender ready and is listening for receiver to connect')

#to accept all incoming connections
clientsocket, address = serversocket.accept()
clientsocket.settimeout(5)
print("Receiver "+str(address)+" connected")

# Do not share and copy code from each other or from Internet
# Please start your code here for sender
x = 0
ackRec = 0
while ackRec != 10:
    try:
        r = "Hello : {}".format(ackRec)
        clientsocket.send(r.encode())
        ack = clientsocket.recv(1024).decode()
        res = 0
        for i in ack:
            if i.isdigit():
                res = int(i)
        if res == ackRec:
            ackRec = ackRec+1
            print(ack)
            time.sleep(0.5)
    except socket.timeout:
        clientsocket.send(r.encode())
        continue
    if ackRec == 10:
        break
serversocket.close()

