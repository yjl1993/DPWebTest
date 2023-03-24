#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/8 19:34
# @Author : jlyu
# @File : testbaidu.py

import time
import os

import allure

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

username = "蛟龙静缘"
password = ""
cookies = {'domain': '.baidu.com', 'expiry': 1608797624, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/',
           'secure': False, 'value': '0c0ka1a0018g2k44ub1fu8ft90r'}, {'domain': '.www.baidu.com', 'expiry': 2554874024,
                                                                      'httpOnly': False, 'name': 'bdime', 'path': '/',
                                                                      'secure': False, 'value': '0'}, {
              'domain': '.www.baidu.com', 'expiry': 2554874024, 'httpOnly': False, 'name': 'ORIGIN', 'path': '/',
              'secure': False, 'value': '0'}, {'domain': '.www.baidu.com', 'expiry': 2554874024, 'httpOnly': False,
                                               'name': 'sug', 'path': '/', 'secure': False, 'value': '3'}, {
              'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False,
              'value': '1428_33243_33306_31253_32970_33284_33286_33350_33313_33312_33311_33310_33309_26350_33308_33307_33240_22158'}, {
              'domain': '.baidu.com', 'expiry': 1867994023, 'httpOnly': True, 'name': 'BDUSS_BFESS', 'path': '/',
              'sameSite': 'None', 'secure': True,
              'value': 'ZTUURkbWhxNGVrZGpWOHhuRWFRQThyNENTUnpNc2c3OWdRd3daZ3g3eW16QXRnSVFBQUFBJCQAAAAAAAAAAAEAAAB-HfQs8tTB-r6y1LUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKY~5F-mP-RfdH'}, {
              'domain': 'www.baidu.com', 'expiry': 1609658024, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/',
              'secure': False, 'value': '123253'}, {'domain': '.baidu.com', 'expiry': 1867994023, 'httpOnly': True,
                                                    'name': 'BDUSS', 'path': '/', 'secure': False,
                                                    'value': 'ZTUURkbWhxNGVrZGpWOHhuRWFRQThyNENTUnpNc2c3OWdRd3daZ3g3eW16QXRnSVFBQUFBJCQAAAAAAAAAAAEAAAB-HfQs8tTB-r6y1LUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKY~5F-mP-RfdH'}, {
              'domain': '.baidu.com', 'expiry': 3756277650, 'httpOnly': False, 'name': 'BAIDUID_BFESS', 'path': '/',
              'sameSite': 'None', 'secure': True, 'value': 'A201C2F155A1F876AC974D05A65F1806:FG=1'}, {
              'domain': '.www.baidu.com', 'expiry': 2554874024, 'httpOnly': False, 'name': 'sugstore', 'path': '/',
              'secure': False, 'value': '0'}, {'domain': '.baidu.com', 'expiry': 1640330003, 'httpOnly': False,
                                               'name': 'BAIDUID', 'path': '/', 'secure': False,
                                               'value': 'A201C2F155A1F876FDFF3D5943CE1A4C:FG=1'}, {
              'domain': '.baidu.com', 'expiry': 3756277650, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/',
              'secure': False, 'value': 'A201C2F155A1F876AC974D05A65F1806'}, {'domain': '.baidu.com',
                                                                              'expiry': 3756277650, 'httpOnly': False,
                                                                              'name': 'PSTM', 'path': '/',
                                                                              'secure': False, 'value': '1608794003'}, {
              'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False,
              'value': '1'}


class TestBaidu:
    """
    百度相关的WEB自动测试用例，用于演示
    """

    @allure.title('登录用例')
    def test_login(self):
        print("开始登录用例")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        driver.find_element_by_css_selector('#u1>a').click()
        driver.implicitly_wait(30)
        driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys(username)
        time.sleep(3)
        driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        time.sleep(3)

        for cookie in cookies:
            cookie_dict = {
                "domain": ".baidu.com",
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            driver.add_cookie(cookie_dict)
        driver.refresh()  # 添加cookies后需要刷新一下网页
        user_name = driver.find_element_by_css_selector('#s-top-username>span.user-name.c-font-normal.c-color-t').text  # 获取登录后的用户名
        assert user_name == username  # 判断登录是否成功
        time.sleep(3)
        driver.close()

    @allure.title("搜索用例")
    def test_search(self):
        print("开始搜索用例")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        for cookie in cookies:
            cookie_dict = {
                "domain": ".baidu.com",
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
        driver.find_element_by_id('kw').send_keys("selenium")
        time.sleep(3)
        driver.find_element_by_id('su').click()
        time.sleep(3)
        driver.close()

    @allure.title("修改搜索结果显示条数用例")
    def test_logout(self):
        print("开始修改搜索结果显示条数用例20条")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.baidu.com/")
        for cookie in cookies:
            cookie_dict = {
                "domain": ".baidu.com",
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
        setting_element = driver.find_element_by_id('s-usersetting-top')
        ActionChains(driver).move_to_element(setting_element).perform()
        time.sleep(3)
        search_setting = driver.find_element_by_link_text("搜索设置")
        ActionChains(driver).move_to_element(search_setting).perform()
        search_setting.click()
        time.sleep(5)
        choice = driver.find_element_by_name("NR")
        choice.find_element_by_xpath('//*[@id="nr_2"]').click()
        time.sleep(3)
        driver.find_element_by_css_selector('#se-setting-7>a.prefpanelgo.setting-btn.c-btn.c-btn-primary').click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)
        driver.find_element_by_id('kw').send_keys("selenium")
        driver.find_element_by_id('su').click()
        time.sleep(3)
        driver.close()

    def test_failcase(self):
        print("一个失败的用例，用于观察报告")
        assert 1 == 2


if __name__ == "__main__":
    test_baidu = TestBaidu()
    test_baidu.test_logout()

    os.system("pytest -s -q  --alluredir=../report/allure-json --clean-alluredir")  # testbaidu.py::TestBaidu::test_failcase
    os.system("allure generate ../report/allure-json -o ../report/allure-report --clean")
    os.system("allure open /Users/bytedance/PycharmProjects/DPWebTest/report/allure-report")
