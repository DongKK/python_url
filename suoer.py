# import requests
# import re
# import os
# class bizhi(object):
#     def qinqiu(self,page):
#         ur='http://desk.zol.com.cn/1920x1080/{}.html'.format(page)
#         head={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.1776'}
#         xy=requests.get(url=ur,headers=head)
#         html=xy.content.decode('gbk')
#         return html
#     def guolv(self,abc):
#         shuju=[]
#         shuju2=[]
#         shuju3=[]
#         shuju4=[]
#         patt=re.compile(r'<li class="photo-list-padding">(.*?)<!--分页-->',re.S)
#         itmes=patt.findall(abc)
#         for i in itmes:
#             shuju.append(i)
#         patt2=re.compile(r'href="(.*?)" target=')
#         for f in range(len(shuju)):
#             itmes2=patt2.findall(shuju[f])
#             for j in itmes2:
#                   shuju2.append(j)
#         patt3 = re.compile(r'/bizhi.*.html', re.S)
#         for j in range(len(shuju2)):
#            itmes3 = patt3.findall(shuju2[j])
#            shuju3.append(itmes3)
#         for q in range(len(shuju3)):
#             shuju4.append(shuju3[q][0])
#         return shuju4
#
#     def mulu(self,abc):
#         shuju=[]
#         b=os.listdir()
#         patt=re.compile(r'<!-- xiongzm end -->(.*?)<!--分页-->',re.S)
#         itmes=patt.findall(abc)
#         for i in itmes:
#             shuju.append(i)
#         patt2=re.compile(r'alt="(.*?)" src=')
#         for j in range(len(shuju)):
#             itmes2=patt2.findall(shuju[j])
#         for h in range(15):
#             if itmes2[h] in b:
#                continue
#             else:
#                 os.mkdir(itmes2[h])
#         return itmes2
#     def dakai(self,jia):
#         ur='https://desk.zol.com.cn{}'.format(jia)
#         head={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.1776'}
#         xy=requests.get(url=ur,headers=head)
#         html=xy.content.decode('gbk')
#         return html
#
#     def guolv2(self,abc):
#         shuju=[]
#         patt=re.compile(r'<ul id="showImg" class="clearfix" style="left:-0px;width:(.*?)</li></ul>			</div>',re.S)
#         itmes=patt.findall(abc)
#         for i in itmes:
#             shuju.append(i)
#         patt2=re.compile(r'https://desk.*?.jpg',re.S)
#         for j in range(len(shuju)):
#            itmes2=patt2.findall(shuju[j])
#            return itmes2
#     def tihuan(self,abc):
#         a=abc
#         b=[]
#         for i in range(len(a)):
#            b.append(a[i].replace('144x90','1280x1024'))
#         return b
#
#     def save(self,abc,mu):
#         os.chdir('C:/Users/DongKK/PycharmProjects/untitled/{}'.format(mu))
#         for i,j in enumerate(abc):
#             res=requests.get(j)
#             bian=res.content
#             with open('{}.jpg'.format(i+1),'wb') as f:
#                # os.chdir('C:/Users/DongKK/PycharmProjects/untitled/{}'.format(mu))
#                f.write(bian)
#             print(j)
#
#


# jg=bizhi()
# jg2=jg.qinqiu(page=0)    #请求
# # print(jg2)
# jg3=jg.mulu(abc=jg2)     #目录
# # print(len(jg3))
# jg4=jg.guolv(abc=jg2)    #第一次过滤
# # print(jg4)
# jg5=jg.dakai(jia=jg4[6])    #打开套图
# # print(jg5)
# jg6=jg.guolv2(abc=jg5)           #第二次过滤
# # print(jg6)
# jg7=jg.tihuan(abc=jg6)    #调整图片大小格式
# # print(jg7)
# jg.save(abc=jg7,mu=jg3[6])
#
#
#
#
#
#
