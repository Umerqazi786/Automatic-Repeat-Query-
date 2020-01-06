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
print("Receiver "+str(address)+" connected")

# Do not share and copy code from each other or from Internet
# Please start your code here for sender

x = 0
message = list()
while x < 10:
    message.append("Hello:{0}".format(x))
    x = x+1
N = input("Enter windowSize: ")
N = int(N)
windowSize = N;
a = 0
ackRec = 0
packet = ''
x = 0
while x < windowSize:
     packet += input() + "|"  # packet + message[x]+'|'
     x = x + 1
print("Sending out packets:")
print("")
print(packet)
print("")

#while a < windowSize:
    #packet = packet + message[a]+'|'
     #a = a + 1

clientsocket.send(packet.encode())
slide = N
Ack = set()
while ackRec < 10:
    recv = set()
    AckRec = set()
    x = 0
    while x < windowSize:
        data = clientsocket.recv(1024).decode()
        print(data)
        for i in data:
            if i.isdigit():
                Ack.add(int(i))
        x = x+1
    print("")
    print("")
    ackRec = len(list(Ack))
    if ackRec == 10:
        break
    if slide + ackRec < 10:
        compare = list(range(0, slide + ackRec))
    else:
        compare = list(range(0,10))
    compare = set(compare)
    recv = compare.difference(Ack) # set after comparison with ack received so far and compare set

    x = 0
    while len(list(recv)) != windowSize:
        if len(recv) is 0:
            recv.add(max(Ack) + 1)
            while max(recv)!=9:
                recv.add(max(recv) + 1)
        if max(recv) == 9:
            break

        recv.add(max(list(recv)) + 1)

    recv = sorted(list(recv))
    remsg = ""
    x = 0
    while x < len(recv):
        remsg += "Hello:{0}".format(recv[x]) + '|'
        x = x + 1
    print("Sending out packets:")
    print("")
    print(remsg)
    print("")



    clientsocket.send(remsg.encode())

serversocket.close()