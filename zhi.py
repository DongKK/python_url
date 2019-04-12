#!/usr/bin/python
#_*_coding='utf-8'_*_
import xlrd
import requests
import unittest
import HTMLTestRunner
class jieguo(object):
    def qinqiu(self,value):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head={'Content-Type':'application/json',
'x-dealer-code':'2100001',
'x-position-code':'D_PO_1028',
'x-resource-code':'pol4s_partOrder_orderPartDetail',
'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
'x-user-code':'dhxc1u',
'x-access-token':'0da5606a534fa727dfd7f502df38be65'}
        body='{"partOrderItemId":%s}' %(value)
        body=body.encode('utf-8')
        xiangyin=requests.post(url,headers=head,data=body)
        abc=xiangyin.json()
        return abc
    def canshu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\DongKK\PycharmProjects\untitled\cde.xlsx')
        sheet = f.sheets()[0]
        num = sheet.nrows
        for i in range(num):
            if i == 0:
                continue
            else:
                shuju.append(sheet.row_values(i))
        return shuju
# print(jieguo().qinqiu(value=3018))
# print(jieguo().canshu())

class yongli(unittest.TestCase):
    vas=jieguo().canshu()
    def test_1(self):
        vad=jieguo()
        ask=vad.qinqiu(self.vas[0][0])
        self.assertEqual(ask['totalSize'],0)
    def test_2(self):
        vad = jieguo()
        ask = vad.qinqiu(self.vas[1][0])
        self.assertEqual(ask['totalSize'], 0)
    def test_3(self):
        vad = jieguo()
        ask = vad.qinqiu(self.vas[2][0])
        self.assertEqual(ask['totalSize'], 0)
    def test_4(self):
        vad = jieguo()
        ask = vad.qinqiu(self.vas[3][0])
        self.assertEqual(ask['totalSize'], 0)
    def test_5(self):
        vad = jieguo()
        ask = vad.qinqiu(self.vas[4][0])
        self.assertEqual(ask['totalSize'], 0)
    def test_6(self):




if __name__=='__main__':
    unittest.main()
# def baobiao(all):
#     suit=unittest.TestSuite()
#     des=unittest.defaultTestLoader.discover(r'C:\Users\DongKK\PycharmProjects\untitled','zhi.py')
#     for i in des:
#         suit.addTest(i)
#     f=open(r'C:\Users\DongKK\PycharmProjects\untitled\cc.html')
#     run=HTMLTestRunner.HTMLTestRunner(title='索赔测试包告',stream=f,description='结果如下',tester='bbs')
#     run.run(suit)
#     f.close()
