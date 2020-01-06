import socket
import re
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))

# Do not share and copy code from each other or from Internet
# Please start your code here for receiver
ackSend = 0
z = 0
prev_z = 0
while ackSend < 10:
    data = s.recv(1024).decode()
    data = data.split("|")
    del data[-1]
    str1 = ""
    if (len(data) + ackSend) < 11:
        compare = list(range(ackSend, len(data) + ackSend))
    else:
        compare = list(range(ackSend, 10))
    recv = list()
    x = 0
    while x < len(data):
        for i in data[x]:
            if i.isdigit():
                recv.append(int(i))
        x = x+1
    x = 0
    while x < len(data):
        time.sleep(0.5)
        if compare[x] == recv[x]:
            print(data[x])

            prev_z = z
            str1 = "Ack:{0}".format(prev_z)
            z = z + 1
            ackSend = ackSend + 1
            s.send(str1.encode())
        elif compare[x] != recv[x]:
            while x < len(data):
                print("")
                str1 = "Ack:{0}".format(prev_z)
                time.sleep(0.5)
                s.send(str1.encode())
                time.sleep(1)
                x = x+1

        if x == len(data):
            break

        x = x+1
        time.sleep(.5)
    print("")
    print("")
    if ackSend == 10:
        break
s.close()