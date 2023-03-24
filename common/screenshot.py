#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/19 11:20
# @Author : jlyu
# @File : screenshot.py

import time
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ScreenShot:

    def __init__(self, driver):
        self.driver = driver

    def screen_shot(self):
        directory_time = time.strftime("%Y-%m-%d")
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S')
        pic_name = ctime + '.png'
        directory_path = os.path.join(os.path.abspath('..'), 'picture', directory_time)
        try:
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            else:
                pass
        except BaseException as msg:
            print("创建截图目录失败：%s" % msg)

        self.driver.get_screenshot_as_file(directory_path + '/' + pic_name)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    screen = ScreenShot(driver)
    driver.get('http://www.baidu.com')
    time.sleep(2)
    screen.screen_shot()
    driver.close()
