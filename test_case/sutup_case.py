#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/28 14:30
# @Author : jlyu
# @File : sutup_case.py

import ast
import time

from selenium import webdriver
from config.read_ini import ReadConfig
from page.yindaoye_page import YDYPage
from page.shujukeshihua_page import SJKSHPage
from page.renyuanguanlixiangkanban_page import RYGLXKBPage


class SetUpCase:
    """运行正式case前的前置操作，如登录DP、关闭首次打开页面的新手引导页面"""
    def setup_case(self):
        read_config = ReadConfig()
        cookies = read_config.get_config("user_info", "cookies_yjl")
        cookies = ast.literal_eval(cookies)
        url = read_config.get_config("env", "cn_net")
        use_ppe = read_config.get_config("env", "use_ppe")
        modheader_path = read_config.get_config("env", "modheader_path")
        if use_ppe == "yes":  # 如果需要在ppe环境，则加载modheader插件
            option = webdriver.ChromeOptions()
            option.add_extension(modheader_path)  # 加载modheader插件
            # option.add_extension('/Users/bytedance/PycharmProjects/DPWebTest/Ranorex-Selocity.crx')  # 加载获取定位元素的插件，方便调试的时候使用
        else:
            option = None
        self.driver = webdriver.Chrome(chrome_options=option)
        #  self.driver.maximize_window()
        if use_ppe == "yes":  # 如果需要在ppe环境，导入和使用ppe泳道配置
            modheader_url = read_config.get_config("env", "modheader_ppe_url")
            self.driver.get(modheader_url)
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_xpath('//*[@id="svelte"]/main/div/div[1]/button[1]').click()
        self.driver.get(url)
        for cookie in cookies:
            cookie_dict = {
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            self.driver.add_cookie(cookie_dict)
        self.driver.refresh()
        self.yindao_page = YDYPage(self.driver)
        self.shujukeshihua_page = SJKSHPage(self.driver)
        self.renyuanguanlixiangkanban_page = RYGLXKBPage(self.driver)
        self.driver.implicitly_wait(30)
        self.yindao_page.xinshouyindaoye().click()  # 关闭新手引导页面
        self.driver.implicitly_wait(30)
        self.yindao_page.yindaotanchuan().click()  # 关闭引导弹窗
        self.driver.implicitly_wait(30)
        return self.driver