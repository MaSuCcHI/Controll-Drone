from socket import socket, AF_INET, SOCK_DGRAM
import time
HOST = ''
PORT = 19798
ADDRESS = "192.168.100.1"
s = socket(AF_INET, SOCK_DGRAM)

isRoop = True
baseMess = b'\x66\x0a\x80\x80\x80\x80\x01\x02\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x03\x99'
controllMessage = b''

def send(mess):
    s.send(mess,(ADDRESS,PORT))

def takeOFF():
    mess = b'\x66\x0a\x80\x80\x80\x80\x01\x02\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x03\x99'
    for i in range(100):
        send(mess)
        if i == 50:
            time.sleep(0.7)
        else:     
            time.sleep(0.002)

def controll():
    while(isRoop):
        send(controllMessage)
    takeOFF()
    s.close()

def inputHandler():
    pass

