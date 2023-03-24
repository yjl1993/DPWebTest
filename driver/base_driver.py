#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/12 20:28
# @Author : jlyu
# @File : base_driver.py

from selenium import webdriver


class BaseDriver:
    """根据输入的浏览器类型返回对应驱动，默认返回chrome驱动"""

    def browser_driver(self, browser=None):
        if browser == "chrome" or browser is None:
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "ie":
            driver = webdriver.Ie()
        else:
            raise print("需要选择浏览器驱动")
        return driver
