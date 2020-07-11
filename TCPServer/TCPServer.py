# server 服务端
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 客户端的socket对象,<socket._socketobject object at 0x1048be830>
        print(self.request)
        print(self.client_address)   # 客户端的地址和IP,('127.0.0.1', 55270)
        # 服务端socketserver对象,<socketserver.ThreadingTCPServer instance at 0x1048eeab8>
        print(self.server)

        print("get connection from : ", self.client_address)

        # 连接后，向客户端返回数据
        self.request.send('hello')
        flag = True
        while flag:
            # 接收客户端发来的数据
            self.data = self.request.recv(4096).strip()
            print(self.data)
            if self.data == 'exit':
                flag = False
            final_data = "input is %s \r\n" % self.data
            # 处理后返回数据
            self.request.sendall(final_data)


h, p = '0.0.0.0', 9999
server = socketserver.ThreadingTCPServer((h, p), MyTCPHandler)
server.serve_forever()
