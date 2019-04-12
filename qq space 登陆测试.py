# ！usr/bin/python
# _*_ coding='utf-8' _*_
from selenium import webdriver
from time import sleep
import xlrd
import unittest
class biao(object):
    def canshu(self):
        shuju=[]
        f=xlrd.open_workbook(r'C:\Users\DongKK\PycharmProjects\untitled\password.xlsx','wb')
        sheet=f.sheets()[0]
        l=sheet.ncols
        for i in range(0,l):
             zhi=sheet.col_values(i)
             shuju.append(zhi)
        return shuju
    def denglu(self,u,p):
        dr=webdriver.Firefox()
        dr.get('https://qzone.qq.com/')
        sleep(1)
        dr.switch_to.frame('login_frame')
        sleep(1)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys(u)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys(p)
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(5)
        dr.quit()






















# print(len(biao().canshu()[0]))



# dr=webdriver.Firefox()
# dr.get('https://qzone.qq.com/')
# sleep(1)
# dr.switch_to.frame('login_frame')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('931785231')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('DK931785231')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()


