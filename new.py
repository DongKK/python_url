# from selenium import webdriver
# from time import sleep
# import unittest
# from ddt import ddt, data, unpack
#
#
#
#
#
# def login(argument, u, p):
#     argument.find_element_by_id('switcher_plogin').click()
#     sleep(5.0)
#     argument.switch_to.default_content()
#     argument.switch_to_frame('login_frame')
#     argument.find_element_by_id("u").send_keys(u)
#     sleep(1.0)
#     argument.find_element_by_id('p').send_keys(p)
#     sleep(1.0)
#     argument.find_element_by_class_name('login_button').click()
#     sleep(1.0)
#     return argument.title
#
#
# @ddt  # 固定写法
# class T1(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Chrome()
#         cls.dr.get(url='https://qzone.qq.com/')
#         cls.dr.implicitly_wait(10.0)
#         cls.dr.switch_to_frame('login_frame')
#
#     def test_1(self):
#         dr.implicitly_wait(10.0)
#         dr.switch_to_frame('login_frame')
#         dr.find_element_by_id('switcher_plogin').click()
#         sleep(5.0)
#         dr.switch_to.default_content()
#         dr.switch_to_frame('login_frame')
#         dr.find_element_by_id("u").send_keys('825069672')
#         sleep(1.0)
#         dr.find_element_by_id('p').send_keys('houec1019')
#         sleep(1.0)
#         dr.find_element_by_class_name('login_button').click()
#         sleep(1.0)
#
#     @data(['825069672, houec1019'])
#     def test_2(self, value):
#         # print(value)
#         a = value[0].split(',')
#         print(a)
#         b = a[0]
#         c = a[1].strip()
#         print(c)
#         d = login(self.dr, b, c)
#         print(d)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#
#
#
#
# import requests
# import xlrd
# import unittest
# import HTMLTestRunner
# class qingqiu(object):
#     def xiangying(self):
#         url='https://mobileqa.dms.saic-gm.com/api/sit/pol4s/pol4sPartOrder/rest/pol4s/partOrder/orderPartDetail'
#         head={'Content-Type':'application/json',
# 'x-dealer-code':'2100001',
# 'x-position-code':'D_PO_1028',
# 'x-resource-code':'pol4s_partOrder_orderPartDetail',
# 'x-track-code':'4320e7d0-cf0c-7ba2-b3fe-1ecb1f15e394',
# 'x-user-code':'dhxc1u',
# 'x-access-token':'da05ee37e5676e7b27972b2892e0fdeb'}
#         body='{"partOrderItemId": 3018}'.encode('utf-8')
#         reponse=requests.post(url,headers=head,data=body)
#         reponse=reponse.json()
#         return reponse
# print(qingqiu().xiangying())
#
#
#
#
#
#
#
#
#
#
# from selenium import webdriver
# dr=webdriver.Firefox
#
# def goo(argument):
#     print(argument)
#
# class T(object):
#     def test_1(self):
#         goo(self.dr)
#
# g=T()
# print(g)

















































