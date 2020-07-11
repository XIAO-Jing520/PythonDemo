import socket
import threading
import time
import GetNICMsg

NICID = 3


SIZE = 1024 * 5
UDP_PORT_FILE = 2021
TCP_IP_ADDRESS = GetNICMsg.find_all_ip()[NICID]
TCP_IP_ADDRESS_MASK = GetNICMsg.find_all_mask()[NICID]

UDP_BROADCAST_PORT_IPADDR = 2022
UDP_BROADCAST_IPADDR = GetNICMsg.get_broad_addr(
    TCP_IP_ADDRESS, TCP_IP_ADDRESS_MASK)


def tcplink(sock, addr):
    img_name = sock.recv(SIZE)
    img_name.decode('utf-8')
    time1 = time.clock()
    print(img_name)
    with open(img_name, 'wb') as f:
        while True:
            data = sock.recv(SIZE)
            if not data:
                break
            else:
                f.write(data)
    sock.close()
    time1 = time.clock() - time1
    print(img_name.decode('utf-8') + "传输完毕" + "耗时：", time1)


sock_broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
for i in range(10):

    sock_broadcast.sendto(TCP_IP_ADDRESS.encode("utf-8"),
                          (UDP_BROADCAST_IPADDR, UDP_BROADCAST_PORT_IPADDR))
    time.sleep(0.5)

# 创建一个socket
sock_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口（这里的ip要在不同的情况下更改）
sock_host.bind(("0.0.0.0", UDP_PORT_FILE))
# 每次只允许一个客户端接入
sock_host.listen(5)
while True:
    print("等待接入")
    sock, addr = sock_host.accept()
    # 建立一个线程用来监听收到的数据
    t = threading.Thread(target=tcplink, args=(sock, addr))
    # 线程运行
    t.start()
