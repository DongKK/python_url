#!/bin/user/python
#_*_coding="utf-8"_*_
import requests
import re
class spider(object):
    def qinqiu(self):
        ur="有页码的网页"
        head={'伪装头部'}
        xy=requests.get(url=ur,headers=head)
        html=xy.content.decode('utf-8')
        return html
    def gl(self,abc):
        shuju=[]
        patt=re.compile(r'过滤条件1(.*?)过滤条件2',re.S)
        itmes=patt.findall(abc)
        for i in itmes:
            i=i.replace('多余的条件','').strip()
            shuju.append(i)
        return shuju
    def xr(self,cde):
        with open('a.txt','a',encoding='utf-8') as f:
            for i in cde:
                f.write(i+'\n')
    




