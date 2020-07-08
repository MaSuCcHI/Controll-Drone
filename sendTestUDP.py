from socket import socket, AF_INET, SOCK_DGRAM
import time
HOST = ''
PORT = 19798
ADDRESS = "192.168.100.1"
s = socket(AF_INET, SOCK_DGRAM)

def send(mes):
    s.sendto(mes,(ADDRESS,PORT))

def takeOFF_ON():
    mess = b'\x66\x0a\x80\x80\x80\x80\x01\x02\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x03\x99'
    for i in range(100):
        send(mess)
        if i == 50:
            time.sleep(1)
        else:     
            time.sleep(0.002)

# 実行後2秒後に離陸，その後3秒後に着陸を行うテスト
def testTakeOFF():
    mess = b'\x66\x0a\x80\x80\x80\x80\x00\x02\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x02\x99'
    for i in range(3000):
        if i == 1000:
            takeOFF_ON()
        if i == 2500:
            takeOFF_ON()
        send(mess)
        time.sleep(0.002)

def main():
    testTakeOFF()
    s.close()

if __name__ == "__main__":
    main()    