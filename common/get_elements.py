#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/14 16:28
# @Author : jlyu
# @File : get_elements.py

import time
import ast

from selenium import webdriver
from config.read_ini import ReadElement
from selenium.common.exceptions import NoSuchElementException


class GetByMethods:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section=None):
        read_ini = ReadElement()
        element = read_ini.get_element(key, section)
        #element = ast.literal_eval(element_str)
        if element is not None:
            by = element.split('>')[0]
            element_by = element.split('>')[1]
            try:
                if by == 'xp':
                    elements = self.driver.find_element_by_xpath(element_by)
                elif by == "css":
                    elements = self.driver.find_element_by_css_selector(element_by)
                elif by == 'id':
                    elements = self.driver.find_element_by_id(element_by)
                elif by == 'classname':
                    elements = self.driver.find_element_by_class_name(element_by)
                elif by == 'name':
                    elements = self.driver.find_element_by_name(element_by)
                elif by == 'text':
                    elements = self.driver.find_element_by_link_text(element_by)
                else:
                    return None
                return elements
            except NoSuchElementException as e:
                print('元素定位失败，异常信息:{}'.format(e))
                ctime = time.strftime('%Y-%m-%d_%H-%M-%S')
                pic_name = ctime + '.png'
                self.driver.save_screenshot(pic_name)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http//:www.baidu.com")
    test = GetByMethods(driver)
    element = test.get_element("baidu", "send_text")
    element.send_keys("selenium")
    time.sleep(3)
    driver.close()
