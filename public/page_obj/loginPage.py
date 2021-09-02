#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os, sys
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from time import sleep
from public.models.GetYaml import getyaml
from public.models.imgCode import getCode
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
testData = getyaml(setting.TEST_Element_YAML + '/' + 'login.yaml')


class login(Page):
    """
    用户登录页面
    """
    url = ''
    # dig_login_button_loc = (By.CSS_SELECTOR, testData.get_elementinfo(0))

    def dig_login(self):
        """
        首页登录
        :return:
        """
        # self.find_element(*self.dig_login_button_loc).click()
        sleep(1)
    # 定位器，通过元素属性定位元素对象
    # 手机号输入框
    login_phone_loc = (By.NAME, testData.get_elementinfo(0))
    # 密码输入框
    login_password_loc = (By.NAME, testData.get_elementinfo(1))
    # 图片验证码
    picture_code_loc = (By.NAME, testData.get_elementinfo(2))
    # picture_code_loc = (getCode())
    # 单击登录
    login_user_loc = (By.ID, testData.get_elementinfo(3))
    # 退出登录
    login_exit_loc = (By.ID, testData.get_elementinfo(4))
    # 选择退出
    login_exit_button_loc = (By.XPATH, testData.get_elementinfo(5))

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
        # self.find_element(*self.picture_code_loc).send_keys(imgCode)
        self.find_element(*self.picture_code_loc).send_keys(imgCode)

    def login_button(self):
        """
        登录按钮
        :return:
        """
        self.find_element(*self.login_user_loc).click()

    def login_exit(self):
        """
        退出系统
        :return:
        """
        above = self.find_element(*self.login_exit_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(2)
        self.find_element(*self.login_exit_button_loc).click()

    def user_login(self, username, password, imgCode):
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
        self.picture_code(imgCode)
        sleep(1)
        self.login_button()
        sleep(1)

    phone_pawd_error_hint_loc = (By.XPATH, testData.get_CheckElementinfo(0))
    user_login_success_loc = (By.ID, testData.get_CheckElementinfo(1))
    exit_login_success_loc = (By.ID, testData.get_CheckElementinfo(2))

    # 手机号或密码错误提示
    def phone_pawd_error_hint(self):
        return self.find_element(*self.phone_pawd_error_hint_loc).text

    # 登录成功信息获取
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text

    # 退出登录
    def exit_login_success_hint(self):
        return self.find_element(*self.exit_login_success_loc).text
