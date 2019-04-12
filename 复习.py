#!/bin/python
#-*-coding:utf-8-*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host=('127.0.0.1',8888)
while True:
      abc=input('请输入点啥：')
      if abc!='exit':
          s.sendto(abc.encode('utf-8'),host)
          a,b=s.recvfrom(1024)
          print(b)
      else:
          break








