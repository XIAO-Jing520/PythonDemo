import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 2020
Message = "Hello, Server"


clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(Message.encode("utf-8"), (UDP_IP_ADDRESS, UDP_PORT_NO))
