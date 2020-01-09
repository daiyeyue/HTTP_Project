import socket

#print(socket.AF_INET)
print(ord('中'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 注意address的书写格式
# 以及tuple两个元素的含义
sock.bind(("127.0.0.1",7777))
print("已经绑定地址和端口")

# 监听
sock.listen()
print("开始建立监听")

# 接受一个传进来的socket
print("正在等待socket传入…………")
skt, address = sock.accept()
print("已经接收到socket {0}".format(skt))

#读取传入消息，实际上是信息
# 需要注意读取信息的长度一定要小于等于实际消息的长度，否则会假死

msg = skt.recv(500)
#print(type(msg)) # 得到的是字符流编码的信息

#decode缺省是使用utf-8
print(msg.decode())

msg = "I love only wangxiaojing"
skt.send(msg.encode())

skt.close()
sock.close()


#读取完成后，给对方一个反馈

