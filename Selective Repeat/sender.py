import socket
import time
import multiprocessing

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
message = list()
while x < 10:
    message.append("Hello:{0}".format(x))
    x = x+1

windowSize = 5;
a = 0
ackRec = 0
packet = ''
x = 0
print("Enter first 5 packets: ")
while x < windowSize:
    packet += input() + "|"  # packet + message[x]+'|'
    x = x + 1
#while a < windowSize:
   # packet = packet + message[a]+'|'
    #a = a + 1
print("Sending out entered packets:")
print("")
print(packet)

clientsocket.send(packet.encode())
Ack = set()
data = ""
while ackRec != windowSize:
    try:
        print("")
        data = clientsocket.recv(1024).decode()
        data = data.split("|")
        del data[-1]
        data = set(data)
        data = sorted(list(data))
    except socket.timeout:
        clientsocket.send(packet.encode())
        continue
    x = 0
    while x < len(data):
        print(data[x])
        time.sleep(0.5)
        for i in data[x]:
            if i.isdigit():
                Ack.add(int(i))
                ackRec = ackRec + 1
        x = x+1
    if ackRec == windowSize:
        ackRec = 0
        Ack.clear()
        break

    check = list(range(5))
    check = set(check)
    diff = check.difference(Ack)
    diff = list(diff)
    x = 0
    remsg = ""
    while x < len(diff):
        remsg += "Hello:{0}".format(diff[x]) + '|'
        x = x + 1

    clientsocket.send(remsg.encode())
packet = ''
x = 0
print("Enter next 5 packets:")
while x < windowSize:
    packet += input() + "|"  # packet + message[x]+'|'
    x = x + 1
print("Sending out entered packets:")
print("")
print(packet)
#while a < 2 * windowSize:
    #packet = packet + message[a]+'|'
    #a = a + 1
clientsocket.send(packet.encode())
           # Ack = set()
while ackRec !=  windowSize:
    try:
        print("")
        data = clientsocket.recv(1024).decode()
        data = data.split("|")
        del data[-1]
        data = set(data)
        data = sorted(list(data))
    except socket.timeout:
        clientsocket.send(packet.encode())
        continue
    x = 0
    while x < len(data):
        print(data[x])
        time.sleep(0.5)
        for i in data[x]:
            if i.isdigit():
                Ack.add(int(i))
                ackRec = ackRec + 1
        x = x+1

    if ackRec == windowSize:
        ackRec = 0
        Ack.clear()
        break

    check = list(range(5,10))
    check = set(check)
    diff = check.difference(Ack)
    diff = list(diff)
    x = 0
    remsg = ""
    while x < len(diff):
        remsg += "Hello:{0}".format(diff[x]) + '|'
        x = x + 1

    clientsocket.send(remsg.encode())
serversocket.close()