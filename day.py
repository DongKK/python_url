



# import  pymysql
# conn=pymysql.connect(host='192.168.0.107',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')

# abc=conn.cursor()
# while True:
#       a=input('>>>>')
#       if a!='exit':
#          abc.execute()
#          print(abc.fetchall())
#       else:
#          break

#conn.close()




import xlrd
# import  pymysql
# conn=pymysql.connect(host='192.168.0.125',
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      charset='utf8')
# f=xlrd.open_workbook('dianying.xls')
# a=f.sheet_by_name('douban')
# abc=conn.cursor()
# for i in range(26):
#     b=a.cell(i,0).value
#     c=a.cell(i,1).value
#     d=a.cell(i,2).value
#     e=a.cell(i,3).value
#     print(type(b))
# abc.execute('use T1;')
# abc.execute('create table dianying (片名 char(20),导演 char(20),评价人数 char(20),描述 char(20));')
    # abc.execute('insert into dianying values ({},{},{},{});'.format(b,c,d,e))

# import pymysql
# import xlrd
# conn = pymysql.connect(host="192.168.0.125",
#                        port = 3306,
#                        user='root',
#                        password="123456",
#                        charset='utf8')
# abc=conn.cursor()
# abc.execute('create database wenjian12 default character set utf8')
# # while True:
# #     try:
# #        a=input("<<<<<<<")
# #        if a=="exit":
# #           conn.close()
# #           break
# #        else:
# #           abc.execute(a)
# #           print(abc.fetchall())
# #     except:
# #         print("你个傻叉")
# abc.execute('use wenjian12;')
# abc.execute('create table   biao4 (aa char(255),bb char(10),cc char(10));')
# f=xlrd.open_workbook("电影.xls")
# print(f.nsheets)
# sheet = f.sheets()[0]
# aa=sheet.nrows
# for i in range(2):
#     a="n"
#     bv="v"
#     b=sheet.row_values(i)
#     nnn=b[1]
#     bbb=b[0]
#     print(b[0],b[1])
# abc.execute('insert into biao4 values  ({},{},{});'.format(bbb,'fulanke',nnn))
#     abc.execute('select * from biao4;')
#     print(abc.fetchall())







#
# import json
# a={'name':123}
# json_data=json.dumps(a)
# print(json_data)
# abc=json.loads(json_data)
# print(abc['name'])



#晚自习干掉
# import xlrd
# import pymysql
# dk=pymysql.connect(host='192.168.0.70',port=3306,user='root',password='123456',charset='utf8')
# f=xlrd.open_workbook('dianying.xls')
# a=f.sheets()[0]
# abc=dk.cursor()
# abc.execute('use T1;')
# for i in range(a.nrows):
#     b=a.row_values(i)
#     if i>=0:
#         abc.execute('create table biao6 ({} char(100),{} char(100),{} char(100),{} char(100));'.format(b[0],b[1],b[2],b[3]))
#     else:
#         abc.execute('insert into biao6 values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
#         dk.commit()
# abc.execute('select * from biao5;')
# print(abc.fetchall())
# dk.close()











# import requests
# import re
# class zlzp_spider(object):
#     def qingqiu(self):
#         ur='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=639&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&_v=0.16993315&x-zp-page-request-id=f5931973fe7e4006b81aa557cbec1979-1550653090198-689773'
#         head={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.1776'}
#         xiangyin=requests.get(url=ur,headers=head)
#         html=xiangyin.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         shuju2=[]
#         patt=re.compile(r'"company".*?公司',re.S)
#         items=patt.findall(abc)
#         for i in items:
#             shuju.append(i)
#         patt2=re.compile(r'.*?公司',re.S)
#         for j in range(len(shuju)):
#             shuju2.append(patt2.findall(shuju[j]))
#         return shuju2
#
#
#
#
#
# fff=zlzp_spider()
# d=fff.qingqiu()
# e=fff.guolv(abc=d)
# print(e)
# # print(type(d))



# a=int(input('>>>>:'))
# b=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# c=[]
# d=''
# while True:
#     b.insert(0,b[a%16])
#     a=a/16
#     if a==0:
#         break
# print(c)



# import pymysql
# import xlwt
# conn=pymysql.connect(host='192.168.0.70',port=3306,user='root',passwd='123456',charset='utf8')
# abc=conn.cursor()
# abc.execute('use T1;')
# abc.execute('select * from biao6;')
# cde=abc.fetchall()
# f = xlwt.Workbook('utf-8')
# bcd=f.add_sheet('学习1')
# for i in range(len(cde)):
#  bcd.write(i,0,cde[i])
# f.save(r'dianying1.xls')
# print(cde[1][1])




# client 客户端


import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
while True:
   sock.connect(('127.0.0.1',8888))
# 发送请求
   reg=input('>>>:')
   sock.send(reg.encode(('utf-8')))
# 接收数据
   msg=sock.recv(1024)
   print(msg.decode('utf-8'))
# 断开连接
   if  reg==exit:
       sock.close()

























