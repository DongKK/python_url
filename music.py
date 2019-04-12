# import requests
# import re
# class music(object):
#     def qingqiu(self,ur):
#         head={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.1776'}
#         xy=requests.get(url=ur,headers=head)
#         html=xy.content.decode('utf-8')
#         return html
#
#
#
#
# jg=music()
# jg1=jg.qingqiu(ur='https://music.163.com/#/playlist?id=2578520695')
# print(jg1)







# import paramiko
# # 创建一个远程客户端
# ssh123=paramiko.SSHClient()
# #第一次连接主机,模块中known_hosts 存放的主机地址         跳过查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# #连接主机
# ssh123.connect(hostname='192.168.0.70',port=22,username='root',password='123456')
# #exec_command 执行命令  直接具有结果的命令
# a,b,c=ssh123.exec_command('pstree')          #第一个变量：输入的命令，第二个变量：命令执行的结果，第三个变量：命令的报错
# #读取并解码
# print(b.read().decode())
# #断开连接
# ssh123.close()



# import paramiko
#传输文件
#建立一个传输通道
# ssh123=paramiko.Transport('192.168.0.70',22)
# #连接linux
# ssh123.connect(username='root',password='123456')
# #创建一个文件传输的对象
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# #从linux到windows传文件
# #第一个参数：表示要传输的文件
# #第二个参数：表示要存放的本机位置
# # sftp.get('install.log',r'.\abc.log')  #非当前目录下的文件需要加路径   #abc.log为传入的命名的文件
#ssh123.close()
#
#
# #从windows到linux
# sftp.put('a.txt',r'/home/bbs.txt')
# ssh123.close()

#
# import paramiko
# with paramiko.SSHClient() as ssh22:
#          ssh22.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#          ssh22.connect(hostname='192.168.0.70',port=22,username='root',password='123456')
#          while True:
#              abc=input('请输入命令:')
#              a,b,c=ssh22.exec_command(abc)
#              print(b.read().decode())
#              if abc=='exit':
#                  break



#
# import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh123.connect(hostname='192.168.0.70',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -al')
# print(b.read().decode())







# socket   自带的模块
# socket:套接字，是实现最底层的一种通信方式     功能： 接收   发送
# 采用的是c/s架构

# 通过tcp协议进行通信   socket

# server端

# import socket
# # 创建一个套接字，并且归档使用tcp协议，ip版本ipv4(AF_INET)   ipv6(AF_INET6)
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 绑定ip、端口号    接收的是个元组
# s.bind(('127.0.0.1',8888))
# # 监听服务是否开启，数字指的是最大等待数
# s.listen(3)
# while True:
#     #接收请求   第一个变量：连接信息， 第二个变量：客户端的ip和端口号
#     e,f=s.accept()
#     #接收数据   1024表示一次性最大能接收1024字节的数据
#     reg=e.recv(1024)
#     print(reg.decode('utf-8'))
# #




# client 客户端
#
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 连接服务器
# sock.connect(('127.0.0.1',8888))
# # 发送请求
# sock.send('hello'.encode(('utf-8')))
# # 接收数据
# msg = sock.recv(1024)
# print(msg.decode('utf-8'))
# # 断开连接
# sock.close()
#




# udp客户端(client)
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#       abc=input('请输入：')
#       if abc!='exit':
#         host=('127.0.0.1',8888)                   #直接发送请求
#         sock.sendto(abc.encode('utf-8'),host)
#         msg=sock.recv(1024)                                     #接收数据
#         print(msg.decode('utf-8'))
#       else:
#           break

























# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('127.0.0.1',8888))
# while True:
#     abc=input('请输入点啥:')
#     if abc!='exit':
#         conn,addr=s.recvfrom(1024)
#         print(conn.decode('utf-8'))
#         s.sendto(abc.encode('utf-8'),addr)
#     else:
#         break





# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 绑定ip
# s.bind(('127.0.0.1',8888))
# while True:
#     abc=input('请输入：')
#     if  abc!='exit':
#       conn,addr=s.recvfrom(1024)      #变量1：客户端发送的请求数据   变量2：ip和端口号
#       print(conn.decode('utf-8'))     #打印接收到的数据
#       s.sendto(abc.encode('utf-8'),addr)     #发送响应
#     else:
#         break



























