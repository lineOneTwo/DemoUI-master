#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page, log
from time import sleep
from public.models.GetYaml import getyaml

from public.models.imgCode import getCode
testData = getyaml(setting.TEST_Element_YAML + '/' + 'work.yaml')


class login(Page):
    """
    用户登录页面
    """
    url = ''

    def dig_login(self):
        """
        登录
        :return:
        """
        sleep(1)

    # 定位器，通过元素属性定位元素对象
    # 手机号输入框
    login_phone_loc = (By.NAME, testData.get_elementinfo(1))
    # 密码输入框
    login_password_loc = (By.NAME, testData.get_elementinfo(2))
    # 图片验证码
    picture_code_loc = (By.NAME, testData.get_elementinfo(3))
    # 单击登录
    login_user_loc = (By.ID, testData.get_elementinfo(4))
    # 事件管理
    event_loc = (By.CSS_SELECTOR, testData.get_elementinfo(5))
    #我受理的事件
    my_events_loc = (By.LINK_TEXT, testData.get_elementinfo(6))
    #完成按钮
    complete_event_loc = (By.CSS_SELECTOR, testData.get_elementinfo(7))
    #完成内容
    complete_content_loc = (By.CSS_SELECTOR, testData.get_elementinfo(8))
    #上传图片按钮
    upload_loc = (By.CSS_SELECTOR, testData.get_elementinfo(9))
    #上传图片
    # upload_file_loc = (By.XPATH, testData.get_elementinfo(9))
    #提交按钮
    submit_loc = (By.CSS_SELECTOR, testData.get_elementinfo(10))
    # 退出登录
    login_exit_button_loc = (By.CSS_SELECTOR, testData.get_elementinfo(11))

    def login_phone(self, username):
        """
        登录手机号
        :param username:
        :return:
        """
        self.find_element(*self.login_phone_loc).send_keys(username)

    def login_password(self, password):
        """
        登录密码
        :param password:
        :return:
        """
        self.find_element(*self.login_password_loc).send_keys(password)

    def picture_code(self, imgCode):
        """
        图片验证码
        :param imgCode:
        :return:
        """
        self.find_element(*self.picture_code_loc).send_keys(imgCode)

    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_user_loc).click()

    def event_button(self):
        """
        菜单事件管理按钮
        """
        self.find_element(*self.event_loc).click()
        sleep(3)

    def my_event_button(self):
        """
        我受理的事件
        """
        self.find_element(*self.my_events_loc).click()
        sleep(3)

    def complete_event(self):
        """
        点击完成按钮
        """
        self.find_element(*self.complete_event_loc).click()

    def complete_content(self, textarea):
        """
        完成内容
        :param textarea:
        :return:
        """
        self.find_element(*self.complete_content_loc).send_keys(textarea)

    def upload_button(self):
        """
        点击上传按钮
        """
        self.find_element(*self.upload_loc).click()
        sleep(3)
        os.system('C:/Users/Administrator/uploadFile.exe')
        log.info("上传文件结果是： {0}".format(os.system('C:/Users/Administrator/uploadFile.exe')))

    # def upload_file(self,filePath):
    #     """
    #     上传文件
    #     """
    #     self.find_element(*self.upload_file_loc).send_keys(filePath)

    def submit(self):
        """
        提交完成
        """
        self.find_element(*self.submit_loc).click()

    # def login_exit(self):
    #     """
    #     退出登录
    #     :return:
    #     """
    #     self.find_element(*self.login_exit_button_loc).click()
    #     sleep(10)

    def user_login(self, username, password):
        """
        登录入口
        :param username: 用户名
        :param password: 密码
        :param imgCode: 图片验证码
        :return:
        """
        self.open()
        self.dig_login()
        self.login_phone(username)
        self.login_password(password)
        self.picture_code(getCode())
        sleep(1)
        self.login_button()
        sleep(1)

    def get_event_list(self,textarea):
        self.event_button()
        self.my_event_button()
        self.complete_event()
        self.complete_content(textarea)
        sleep(2)
        self.upload_button()
        # sleep(5)
        # self.upload_file(filePath)
        sleep(3)
        self.submit()



    phone_pawd_error_hint_loc = (By.XPATH, testData.get_CheckElementinfo(0))
    user_login_success_loc = (By.CLASS_NAME, testData.get_CheckElementinfo(1))
    # exit_login_success_loc = (By.ID, testData.get_CheckElementinfo(2))

    # 手机号或密码错误提示
    def phone_pawd_error_hint(self):
        return self.find_element(*self.phone_pawd_error_hint_loc).text

    # 登录成功用户名
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text

    # 退出登录
    # def exit_login_success_hint(self):
    #     return self.find_element(*self.exit_login_success_loc).text
