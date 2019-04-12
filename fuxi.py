# #!/user/bin/python
# #-*-coding:utf-8-*-
# # import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # s.bind('127.0.0.1',8888)
# # s.listen(3)
# # while True:
# #     a,b=s.accept()
#
#
#
#
# # #udp server端
# # import socket
# # s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # # 绑定ip
# # s.bind(('127.0.0.1',8888))
# # while True:
# #     abc=input('请输入：')
# #     if  abc!='exit':
# #       conn,addr=s.recvfrom(1024)      #变量1：客户端发送的请求数据   变量2：ip和端口号
# #       print(conn.decode('utf-8'))     #打印接收到的数据
# #       s.sendto(abc.encode('utf-8'),addr)     #发送响应
# #     else:
# #         break
#
#
#
# # import socket
# # a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # a.connect(('127.0.0.1',8888))
# # a.send('hello'.encode('utf-8'))
# # a.recv(1024)
# # a.close()
#
#
#
#
# import smtplib
# import email.mime.multipart
# import email.mime.text
# server='stmp.163.com'
# user_from='18037600356@163.com'
# user_to='15225356661@163.com'
# sqm='wsnibaba'
# message=email.mime.multipart.MIMEMultipart()
# message['From']=user_from
# message['To']=user_to
# message['subject']='day1'
# text="""
# hello word
# """
# tet=email.mime.text.MIMEText(text,'plian','utf-8')
# message.attach(tet)
# lj=smtplib.SMTP_SSL(server,465)
# lj.login(user_from,sqm)
# lj.sendmail(user_from,user_to,message.as_string())
# lj.close()




























