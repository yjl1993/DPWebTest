#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/24 15:09
# @Author : jlyu
# @File : get_cookies.py

import time

from selenium import webdriver


def get_cookies():
    driver = webdriver.Chrome()
    driver.get("https://datapower.bytedance.net")
    time.sleep(40)  # 留足够时间用来登录
    new_cookies = driver.get_cookies()
    print(new_cookies)


if __name__ == "__main__":
    get_cookies()
