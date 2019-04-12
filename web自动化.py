#！/usr/bin/python
#_*_coding='utf-8'_*_
#web测试环境搭建
#1、需要安装python
#2、安装selenium模块
#3、下载浏览器驱动

# from selenium import webdriver
# from time import sleep
# dr = webdriver.Firefox()           #定义使用某个浏览器
# dr.get('https://www.bilibili.com')    #打开网址
# print(dr.title)                 #获取网址的标题
# sleep(2)
# dr.get('https://www.jd.com')
# sleep(2)
# dr.back()                        #返回
# sleep(2)
# dr.forward()                    #前进
# sleep(2)
# dr.set_window_size(400,400)      #设置浏览器大小
# dr.set_window_position(600,500)   #设置浏览器位置
# sleep(2)
# dr.maximize_window()             #窗口最大化
# sleep(2)
# dr.minimize_window()            #窗口最小
# print(dr.current_url)          #获取打开网页的网址
# sleep(2)
# dr.quit()                     #关闭浏览器,断开连接
# dr.close()            #关闭浏览器不断开连接


#定位
#1.id=’值‘ class=’值‘ 等称之为属性

# dr.find_element_by_id('kw').send_keys('bilibili')    #1.通过id来定位
# sleep(1)
# dr.find_element_by_id('su').click()                 #点击’百度一下‘


#2.class_name来定位  通过标签的class属性来定位的
# dr.find_element_by_class_name('s_ipt').send_keys('bilibili')
# sleep(1)
# dr.find_element_by_class_name('').click()

#3.通过name定位  标签上的那么属性定位
# dr.find_element_by_name('wd').send_keys('wlop')

#4.link_text定位  标签文本定位
# dr.find_element_by_link_text('hao123').click()

#5.partial_link_text定位   标签的模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()

#6.tag_name  定位    通过标签的名称来定位  ，最不唯一的定位，通常用来定位一组数据
# dr.find_element_by_tag_name('')

# 7.css_selector    通过css来定位
# dr.find_element_by_css_selector('#kw').send_keys('wlop')

#8.xpath定位           路径定位
#xpath  路径标记语言
#xml    可扩展性标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('wlop')

#定位准确优先级：id > css > xpath > name > class_name...




# dr.switch_to_frame('login_frame')

# from selenium import webdriver
# import time
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# time.sleep(1)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_id('switcher_plogin').click()
# time.sleep(1)
# dr.find_element_by_id('u').send_keys('931785231')
# time.sleep(1)
# dr.find_element_by_id('p') .send_keys('DK931785231')
# time.sleep(1)
# dr.find_element_by_id('login_button').click()





#定位一组对象
# from selenium import webdriver
# import time
# dr=webdriver.Firefox()
# dr.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# time.sleep(2)
#
# # wd=dr.find_elements_by_class_name('mnav')       #定位一组数据  对多个数据进行操作时
#
# #层级定位      遇到复杂的元素的定位
#
# wd=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in wd:
#     i.click()
#     time.sleep(2)



#模拟动作
#send_keys() 输入
#click（）   点击
#text       获取定位到的元素的文本
#clear（）  清空定位到的元素上面的数据



#处理框架   iframe(窗口)
# dr.switch_to.frame(‘login_frame')             切换框架
# dr.switch_to.frame()   括号里面可以写框架的id属性 name属性  或者先定位到框架
#dr.switch_to.default_content()    #回到最初的页面
# dr.switch_to.parent_frame()               #回到父框架中






# 京东加入购物车

from  selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
dr=webdriver.Firefox()
dr.get('https://www.jd.com/')



#智能等待（设置一个最大等待时间，检测某个元素出现，就不会继续等待）
# unit=ui.WebDriverWait(dr,10)
# # 直到定位的元素出现，就不等待了
# unit.until(lambda dr:dr.find_element_by_xpath(''))
# print('hello')

sleep(2)

# 获取某个元素的值
# w=dr.find_element_by_xpath('/html/head/link[4]')
# a=w.get_attribute('rel')
# print(a)


# 截图      dr.get_screenshot_as_file('图片名称加格式')


#处理浏览器窗口
#获取当前窗口的字符串(句柄)
# dr.get('http://www.lwfree.cn/yurenjie/yuerenjie1.html')
# sleep(2)
# dr.find_element_by_class_name('link-login').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/a').click()
# sleep(1)
# dr.find_element_by_name('loginname').send_keys('18037600356')
# sleep(1)
# dr.find_element_by_name('nloginpwd').send_keys('DK931785231')
# sleep(2)
# dr.find_element_by_id('loginsubmit').click()
# sleep(2)

# start=dr.find_element_by_xpath('')
# sleep(2)
# # drag_and_drop(起始位置，结束位置)
# # drag_and_drop_by_offset（起始位置x轴,y轴坐标）
# ActionChains(dr).drag_and_drop_by_offset(start,156,0).perform()
#处理弹出框

#切换到弹出框
# ww=dr.switch_to.alert
#h获取弹出框上面的内容
# while True:
   # print(ww.text)
#点击确定
   # ww.accept()
#点击取消
   # ww.dismiss()
#输入
   # ww.send_keys('内容')
   # sleep(2)


# 执行javascript(滑动窗口)
# for i in range(1,10000,2000):
#        js="var q=document.documentElement.scrollTop=1000"
#        dr.execute_script(js)       #执行javascript语句
#        sleep(2)














# sleep(10)
# dr.find_element_by_id('key').send_keys('python')
# sleep(2)
# dr.find_element_by_class_name('button').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[7]/a[3]').click()

# # 获取当前窗口的字符串(句柄)
# print(dr.current_window_handle)
# # 获取所有的句柄
# print(dr.window_handles)
# qq=dr.window_handles
# # 切换句柄
# dr.switch_to.window(qq[-1])
# print(dr.title)




# 淘宝加入购物车
# from time import sleep
# from selenium import webdriver
# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('931785231')
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('DK931785231')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# # dr.switch_to.frame('qz-inputer bor2')
# # sleep(2)
# dr.find_element_by_class_name('textinput textarea c_tx3').send_keys('bbb')



#模拟鼠标的操作
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# dr=webdriver.Firefox()
# dr.maximize_window()
# dr.get('https://www.jd.com')
# sleep(2)

# w=dr.find_element_by_xpath('//*[@id="J_cate"]')
# for i in w:
# ActionChains(dr).move_to_element(w).perform()       #动作链（鼠标）控制鼠标来移动到元素的位置上
# sleep(2)









