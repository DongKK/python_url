#
#
#
#

# from appium import webdriver
# import time
#
#
# desired_caps={'platformName':'Android',                 #测试的系统
#               'deviceName':'127.0.0.1:60002',           #测试的设备名
#               'appPackage':'com.netease.cloudmusic',              #测试的安装包
#               'appActivity':'.activity.LoadingActivity'}           #activity的值
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
#
#
# time.sleep(12)
#
# # driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
# # time.sleep(3)
# # driver.find_element_by_id('com.netease.cloudmusic:id/aev').click()
# # time.sleep(3)
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
# time.sleep(2)
# driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15800364149')
# time.sleep(1)
# driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('weilai1258')
# time.sleep(1)
# driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
# time.sleep(2)
# # driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()        #点击抽屉菜单
# # time.sleep(2)
# # driver.find_element_by_id('com.netease.cloudmusic:id/bbn').click()
# # time.sleep(2)
# # driver.find_element_by_id('com.netease.cloudmusic:id/a12').click()
# # time.sleep(2)
# aa=driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
# # print(aa)
# if aa=="贤者破面":
#     print("pass")
# else:
#     print("fail")
# driver.quit()
#




# 断言

# driver.quit()



# time.sleep(30)
# print('手机登陆')
# driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()
# time.sleep(5)
# print('输入手机号')


import time
from appium import webdriver
from time import sleep
import unittest
class wy_music(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',  # 测试的系统
                        'deviceName': '127.0.0.1:60002',  # 测试的设备名
                        'appPackage': 'com.netease.cloudmusic',  # 测试的安装包
                        'appActivity': '.activity.LoadingActivity'}  # activity的值
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(15)
        driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        time.sleep(1)
        driver.find_element_by_id('com.netease.cloudmusic:id/ik').send_keys('15800364149')
        time.sleep(1)
        driver.find_element_by_id('com.netease.cloudmusic:id/ii').send_keys('weilai1258')
        time.sleep(3)
        driver.find_element_by_id('com.netease.cloudmusic:id/qc').click()
        time.sleep(2)
        # driver.find_element_by_id('com.netease.cloudmusic:id/qn').click()
        aa = driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
        # return aa
#     def test_1(self):
#         aa=wy_music().setUp()
#         self.assertNotIn(aa,'dkk')
# if __name__=='__main__':
#     unittest.main()

# print(wy_music().setUp())










# from appium import webdriver
# import time
#
#
# desired_caps = {'platformName': 'Android',
# #                'platformVersion':'6.0',
#                 'deviceName':'127.0.0.1:62001',
#                 'appPackage':'com.netease.cloudmusic',
#                 'appActivity':'.activity.LoadingActivity'}
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# time.sleep(15)
# driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()#点击手机号登录
# time.sleep(5)
# driver.find_element_by_id("com.netease.cloudmusic:id/ik").send_keys("15537831769")#输入手机号
# time.sleep(3)
# driver.find_element_by_id("com.netease.cloudmusic:id/ii").send_keys("gao19930903")#输入密码
# time.sleep(3)
# driver.find_element_by_id("com.netease.cloudmusic:id/qc").click()#点击登录
# time.sleep(10)
# #断言
# driver.find_element_by_id("com.netease.cloudmusic:id/qn").click()  #点击抽屉菜单
# time.sleep(3)
# aa=driver.find_element_by_id("com.netease.cloudmusic:id/af4").text
# if aa=="亚的网易云没有名":
#     print("pass")
# else:
#     print("fail")
# driver.quit()
# print(aa)












