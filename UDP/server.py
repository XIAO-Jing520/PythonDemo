import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 2020

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
    data, addr = serverSock.recvfrom(1024)
    img_str = data.decode()
