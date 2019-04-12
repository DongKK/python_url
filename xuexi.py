#!/usr/bin/python
#_*_coding='utf-8'_*_
import requests
import HTMLTestRunner
import unittest
class qingqiu(unittest.TestCase):
    def test_1(self):
        url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
        head={'Content-Type':'application/json',
              'x-dealer-code':'2100001',
              'x-position-code':'D_PO_1028',
              'x-resource-code':'pol4s_partOrder_orderPartDetail',
              'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
              'x-user-code':'dhxc1u',
              'x-access-token':'0da5606a534fa727dfd7f502df38be65'}
        body='{"partOrderItemId": "3108"}'.encode('utf-8')
        xiangying=requests.post(url,headers=head,data=body)
        res=xiangying.json()
        self.assertEqual(res['errMsg'],'处理成功')
#         print(res)
# print(qingqiu().test_1())
suit=unittest.TestSuite()
suit.addTest(qingqiu('test_1'))
f=open('noheart.html','wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告')

