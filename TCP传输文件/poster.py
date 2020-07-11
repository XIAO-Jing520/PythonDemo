import socket
import threading
from time import sleep

UDP_IP_ADDRESS = None
UDP_PORT_NO = 2020
UDP_PORT_FILE = 2021
UDP_BROADCAST_PORT_IPADDR = 2022


class post_thread (threading.Thread):
    def __init__(self, picture_name):
        threading.Thread.__init__(self)
        self.picture_name = picture_name
        self.sock_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock_host.connect((UDP_IP_ADDRESS, UDP_PORT_FILE))

    def run(self):
        self.sock_host.send(self.picture_name.encode('utf-8'))
        sleep(0.1)
        with open(self.picture_name, 'rb') as f:
            while True:
                data = f.read(1024 * 5)
                if not data:
                    break

                self.sock_host.send(data)

        self.sock_host.close()
        print(self.picture_name + "传输完毕")


thread_list = []
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(("127.0.0.1", UDP_PORT_NO))


temp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
temp_sock.bind(("0.0.0.0", UDP_BROADCAST_PORT_IPADDR))
print("等待告知发送地址")
data, addr = temp_sock.recvfrom(1024)
UDP_IP_ADDRESS = data.decode('utf-8')
print("图片发往:", UDP_IP_ADDRESS)


while True:
    print("等待接入")
    data, addr = serverSock.recvfrom(1024)
    img_str = data.decode()
    thread_list.append(post_thread(img_str))
    thread_list[-1].start()
