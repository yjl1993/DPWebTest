#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 20:30
# @Author : jlyu
# @File : test.py
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# 打开chrome浏览器
driver = webdriver.Chrome()
# 访问百度首页
cookies = {'domain': 'datapower.bytedance.net', 'expiry': 1645326580, 'httpOnly': True, 'name': 'SECURE_SHARE_SESSION_ID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'GBGRV53X24IZK4FJBKLSPEFXLBZZBPJKYRBTZEYDHB253WZN6XUQ'}, {'domain': '.datapower.bytedance.net', 'expiry': 1650510581, 'httpOnly': False, 'name': 'MONITOR_WEB_ID', 'path': '/', 'secure': False, 'value': 'yujialong@bytedance.com'}, {'domain': 'datapower.bytedance.net', 'expiry': 1645326580, 'httpOnly': True, 'name': 'SHARE_SESSION_ID', 'path': '/', 'secure': True, 'value': 'GBGRV53X24IZK4FJBKLSPEFXLBZZBPJKYRBTZEYDHB253WZN6XUQ'}, {'domain': '.datapower.bytedance.net', 'expiry': 1643339370, 'httpOnly': False, 'name': '_tea_utm_cache_2500', 'path': '/', 'secure': False, 'value': 'undefined'}, {'domain': '.datapower.bytedance.net', 'expiry': 1643339381, 'httpOnly': False, 'name': '_tea_utm_cache_5198', 'path': '/', 'secure': False, 'value': 'undefined'}, {'domain': 'datapower.bytedance.net', 'expiry': 1643339370, 'httpOnly': False, 'name': '_xsrf_token', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'db83be3e-2d1c-48f8-28d2-5ecf0802cd7f'}
driver.get("https://datapower.bytedance.net/bi/recent")
time.sleep(2)
# savedCookies = driver.get_cookies()
# print(savedCookies)
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
#driver.maximize_window()
time.sleep(8)
driver.find_element_by_xpath('//*[@id="dialog-0"]/div/div/button').click()  # 关闭新手引导页面
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div/div[3]/button').click()  # 关闭引导弹窗
time.sleep(3)
keshihua = driver.find_element_by_xpath("/html//div[@id='audit-semi-header']/div/div[@class='semi-navigation-inner']//ul[@class='semi-navigation-list']/li[2]/div/div[@class='semi-navigation-item-inner']/span[@class='semi-navigation-item-text']")
ActionChains(driver).move_to_element(keshihua).perform()  # 鼠标移动到数据可视化模块
time.sleep(4)
driver.find_element_by_xpath("/html/body//div[@class='semi-portal-inner']/div//ul[@class='semi-dropdown-menu']/li[2]").click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="data-power-app"]/section/div/div[2]/div[1]/div/div[1]/div[2]').click()
# 我关注的
driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@class='k4hzp semi-tabs semi-tabs-top']/div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[1]//span[@class='semi-tree-option-label-text']").click()
time.sleep(4)
#人员管理向
driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[2]//span[@class='semi-tree-option-label-text']").click()
time.sleep(8)
tetx = driver.find_element_by_xpath("/html//div[@id='data-power-app']/section[@class='semi-layout']/div[@class='content-wrap']/div[@class='_1S7Q7 home_container']//div[@class='semi-row']/div[3]//div[@class='_2Pwh8']").text
assert tetx == "CQC"  # 判断该页面包含CQC字体



#进入cqc看板
#driver.find_element_by_xpath("/html//div[@id='data-power-app']/section[@class='semi-layout']/div[@class='content-wrap']/div[@class='_1S7Q7 home_container']//div[@class='semi-row']/div[3]//button[@type='button']").click()
#time.sleep(4)
# #进入部门全指标统计
# driver.find_element_by_xpath("/html//div[@id='data-power-app']/section[@class='semi-layout']/div[@class='content-wrap']/div[@class='_1S7Q7 home_container']//div[@class='semi-tabs semi-tabs-top']/div[@role='tab-list']/div[2]").click()
# time.sleep(4)
# #分部门核心数据
# driver.find_element_by_xpath("/html//div[@id='data-power-app']/section[@class='semi-layout']/div[@class='content-wrap']/div[@class='_1S7Q7 home_container']//div[@class='semi-tabs semi-tabs-top']/div[@role='tab-list']/div[1]").click()
# time.sleep(8)
# #效率分析
# driver.find_element_by_xpath("/html//div[@id='coreScenarioAnalysis']//div[@role='tab-list']/div[2]//div[@class='_3RCuO']").click()
# time.sleep(4)
# #业务要求
# driver.find_element_by_xpath("/html//div[@id='coreScenarioAnalysis']/div[@class='_2WBC8']/div[@class='content']//div[@role='tab-list']/div[3]//div[.='91 %']").click()
# time.sleep(4)
# #质量分析
# driver.find_element_by_xpath("/html//div[@id='coreScenarioAnalysis']//div[@role='tab-list']/div[4]//div[@class='_3RCuO']").click()
# time.sleep(4)
# #业务管理向看板
# driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[3]//span[@class='semi-tree-option-label-text']").click()
# time.sleep(4)
# # 业务线看板
# driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[4]//span[@class='semi-tree-option-label-text']").click()
# time.sleep(4)
# #进入抖音业务线
# driver.find_element_by_xpath("/html//div[@id='data-power-app']/section[@class='semi-layout']/div[@class='content-wrap']/div[@class='_1S7Q7 home_container']//div[@class='_MIZr']/div[2]/div[@class='semi-spin-children']/div[1]/div[1]//div[@class='_1fIuT']").click()
# time.sleep(4)
# #douyinjuhe
# driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[5]//span[@class='semi-tree-option-label-text']").click()
# time.sleep(4)
# #duiliejuhe
# driver.find_element_by_xpath("//div[@id='data-power-app']/section[@class='semi-layout']//div[@role='tab-content']/div[2]//div[@role='list-box']/div[@role='tree']/li[6]//span[@class='semi-tree-option-label-text']").click()
# #