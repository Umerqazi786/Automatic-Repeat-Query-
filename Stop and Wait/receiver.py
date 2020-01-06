import socket
import re
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))
x = 0;
ackSend = 0
ack = set()
while ackSend != 10:
    data = s.recv(1024).decode()
    for i in data:
        if i.isdigit():
            if int(i) not in ack:
                print(data)
                time.sleep(0.5)
                str1 = "Ack : {0}".format(int(i))
                ack.add(int(i))
                s.send(str1.encode())
                ackSend = ackSend + 1
            else:
                continue
    if ackSend == 10:
        break

s.close()

# Do not share and copy code from each other or from Internet
# Please start your code here for receiver
