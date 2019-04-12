# !/usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
import time
import HTMLTestRunner
class request1(unittest.TestCase):
      def test_1(self):
          self.assertEqual(1,3)
      def test_2(self):
          self.assertEqual(8,2)
      def test_3(self):
          self.assertEqual(9,4)

#创建一个测试套件
suit=unittest.TestSuite()
#添加测试用例
for i in  range(1,4):
      suit.addTest(request1('test_{}'.format(i)))
      now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
f=open('cde.html','wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='索赔测试报告',tester='DK',description='结果如下')
runner.run(suit)
f.close()





