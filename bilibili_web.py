#!usr/bin/python
#_*_ coding='utf-8'_*_
# from selenium import webdriver
# from time import sleep
# class denglu(object):
#     def qinqiu(self):
#         dr=webdriver.Firefox()
#         dr.get('https://www.bilibili.com')
#         sleep(2)
#         dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[3]/div[3]/ul/li[1]/a/div/img').click()
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="login-username"]').send_keys('18037600356')
#         sleep(2)
#         dr.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('DK931785231')
#         sleep(10)
#         dr.find_element_by_xpath('/html/body/div/div/div[2]/div[3]/div[3]/div/div/ul/li[5]/a[1]').click()
#         return dr.title
#
#
#
# denglu().qinqiu()


# import unittest
# import requests
# class jiekou(object):
#     def qingqiu(self,abc=3018):
#         url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
#         head={'Content-Type':'application/json',
# 'x-dealer-code':'2100001',
# 'x-position-code':'D_PO_1028',
# 'x-resource-code':'pol4s_partOrder_orderPartDetail',
# 'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
# 'x-user-code':'dhxc1u',
# 'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
#         body='{ "partOrderItemId":%s}' %(abc)
#         body=body.encode('utf-8')
#         json=requests.post(url,headers=head,data=body)
#         json=json.json()
#         return json
#     def canshu(self):
#         shuju=['3018','123','456','qwe','']
#         return shuju
#
#
# class jiekou_2(object):
#     def qingqiu(self,abc=1):
#         url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrderSearch/partOrderDetailSearch?pageNum=1&pageSize=2&queryTerms=3'
#         head={'Content-Type':'application/json',
# 'x-dealer-code':'2100005',
# 'x-position-code':'D_PO_1028',
# 'x-resource-code':'pol4s_partOrderSearch_partOrderDetailSearch',
# 'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
# 'x-user-code':'dhxc1u',
# 'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
#         body='{"pageNum":%s,"pgeSize":"10","queryTerms":{"orderNo":"V2100880181219390"}}' %(abc)
#         body=body.encode('utf-8')
#         json=requests.post(url,headers=head,data=body)
#         json=json.json()
#         return json
#     def canshu(self):
#         shuju=['3018','123','456','qwe','']
#         return shuju
# # print(jiekou_2().qingqiu())
#
# class  yongli(unittest.TestCase):
#     abc=jiekou().canshu()
#     def test_1(self):
#         suo=jiekou()
#         answer=suo.qingqiu(self.abc[0])
#         self.assertEqual(answer['totalSize'],0)
#     def test_2(self):
#         suo=jiekou()
#         answer=suo.qingqiu(self.abc[1])
#         self.assertEqual(answer['totalSize'],0)
#     def test_3(self):
#         suo=jiekou()
#         answer=suo.qingqiu(self.abc[2])
#         self.assertEqual(answer['totalSize'],0)
#     def test_4(self):
#         suo=jiekou()
#         answer=suo.qingqiu(self.abc[3])
#         self.assertEqual(answer['totalSize'],0)
#     def test_5(self):
#         suo=jiekou()
#         answer=suo.qingqiu(self.abc[4])
#         self.assertEqual(answer['totalSize'],0)
# if __name__=='__main__':
#     unittest.main()



# print(jiekou().canshu())
# print(jiekou().qingqiu())



