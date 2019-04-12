#！/usr/bin/python
#_*_ coding=utf-8_*_
from appium import webdriver
from time import sleep
sleep(2)
caps={'platformName':'Android',
      'deviceName':'127.0.0.1:60001',
      'appPackage':'tv.danmaku.bili',
      'appActivity':'.ui.splash.SplashActivity'}
dr=webdriver.Remote('http://localhost:4723/wd/hub',caps)
# dr.find_element_by_class_name()




