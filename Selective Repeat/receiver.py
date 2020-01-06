import socket
import re
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))

# Do not share and copy code from each other or from Internet
# Please start your code here for receiver
windowSize = 5
ackSend = 0
while ackSend != windowSize:
    print("")
    data = s.recv(1024).decode()
    print( "Packets Received")
    print("")
    print(data)
    print("")
    data = data.split("|")
    del data[-1]
    data = set(data)
    data = sorted(list(data))
    str1 = ""
    x = 0
    while x < len(data):
        res = re.findall('\d+',data[x])
        res = map(int,res)
        d = max(res)
        if d <  windowSize:
            print(data[x])
            time.sleep(0.5)
            str1 += "Ack:{0}".format(d) + '|'
            ackSend = ackSend + 1
        x = x+1

    s.send(str1.encode())
    if ackSend == windowSize:
        ackSend = 0
        break
while ackSend !=  windowSize:
    print("")
    data = s.recv(1024).decode()
    print("Packets Received")
    print("")
    print(data)
    print("")
    data = data.split("|")
    del data[-1]
    data = set(data)
    data = sorted(list(data))
    str1 = ""
    x = 0
    while x < len(data):
        res = re.findall('\d+', data[x])
        res = map(int, res)
        d = max(res)
        if d < 2 * windowSize and d > 4:
            print(data[x])
            time.sleep(0.5)
            str1 += "Ack:{0}".format(d) + '|'
            ackSend = ackSend + 1
        x = x + 1

    s.send(str1.encode())
    if ackSend == windowSize:
        break


s.close()