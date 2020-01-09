# fp = r'.\webapp\hello.html'
# with  open(fp, mode='r', encoding='utf-8') as f:
#     data = f.read()
#     print(data.encode())
#     print(data.encode().decode())
#
# fp = r'.\webapp\daiye.txt'
# with  open(fp, mode='r', encoding='utf-8') as f:
#     data = f.read()
#     print(data.encode())
#
# msg = '我爱北京图灵学院'
# print(msg.encode())
# msg = b'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\x9b\xbe\xe7\x81\xb5\xe5\xad\xa6\xe9\x99\xa2'
# print(msg.decode())

import socket
fp = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>北京图灵学院欢迎您</title>
</head>
<body>

<h1 style="color:blue"> 我爱北京图灵学院刘大拿</h1>

</body>
</html>
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen()
skt, address = sock.accept()
msg = skt.recv(500)
#print(type(msg)) # 得到的是字符流编码的信息

#decode缺省是使用utf-8
print(msg.decode(encoding='gbk'))

msg = "我爱北京图灵学院刘大拿"
skt.send(str())
skt.send(fp.encode())

skt.close()
sock.close()
#print(fp)

bytes('HTTP/1.1 201 OK\r\n\r\n', 'utf8')
