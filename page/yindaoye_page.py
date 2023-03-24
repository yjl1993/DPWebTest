#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/26 11:36
# @Author : jlyu
# @File : yindaoye_page.py

import time

from selenium import webdriver
from common import get_elements


class YDYPage:

    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def xinshouyindaoye(self):
        '''新手引导页'''
        return self.get_elements.get_element("yindaoye", "xinshouyindaoye")

    def yindaotanchuan(self):
        '''引导页弹窗'''
        return self.get_elements.get_element("yindaoye", "yindaotanchuan")

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://datapower.bytedance.net")
    cookies = {'domain': 'datapower.bytedance.net', 'expiry': 1645326580, 'httpOnly': True,
               'name': 'SECURE_SHARE_SESSION_ID', 'path': '/', 'sameSite': 'None', 'secure': True,
               'value': 'GBGRV53X24IZK4FJBKLSPEFXLBZZBPJKYRBTZEYDHB253WZN6XUQ'}, {'domain': '.datapower.bytedance.net',
                                                                                  'expiry': 1650510581,
                                                                                  'httpOnly': False,
                                                                                  'name': 'MONITOR_WEB_ID', 'path': '/',
                                                                                  'secure': False,
                                                                                  'value': 'yujialong@bytedance.com'}, {
                  'domain': 'datapower.bytedance.net', 'expiry': 1645326580, 'httpOnly': True,
                  'name': 'SHARE_SESSION_ID', 'path': '/', 'secure': True,
                  'value': 'GBGRV53X24IZK4FJBKLSPEFXLBZZBPJKYRBTZEYDHB253WZN6XUQ'}, {
                  'domain': '.datapower.bytedance.net', 'expiry': 1643339370, 'httpOnly': False,
                  'name': '_tea_utm_cache_2500', 'path': '/', 'secure': False, 'value': 'undefined'}, {
                  'domain': '.datapower.bytedance.net', 'expiry': 1643339381, 'httpOnly': False,
                  'name': '_tea_utm_cache_5198', 'path': '/', 'secure': False, 'value': 'undefined'}, {
                  'domain': 'datapower.bytedance.net', 'expiry': 1643339370, 'httpOnly': False, 'name': '_xsrf_token',
                  'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'db83be3e-2d1c-48f8-28d2-5ecf0802cd7f'}

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
        driver.add_cookie(cookie_dict)
    driver.refresh()
    time.sleep(5)
    YDYPage(driver).get_elements.get_element("yindaoye", "xinshouyindaoye").click()
    driver.implicitly_wait(30)
    #ydy.xinshouyindaoye()