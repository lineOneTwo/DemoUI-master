#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'


from .driver import browser
import unittest
from selenium import webdriver

class MyTest(unittest.TestCase):
    """
    自定义MyTest类
    """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        #cls.driver.get('http://sqwytst.wt.com:14352/')
        cls.driver.get('http://sqwy.wt.com:5130/')
        cls.driver.find_element_by_css_selector('.login_btn').click()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.save_screenshot("share/screeshots/screenshot/1.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
