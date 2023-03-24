#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/16 16:19
# @Author : jlyu
# @File : webdriver_api.py

import time

from selenium import webdriver

# 打开chrome浏览器
driver = webdriver.Chrome()
# 访问百度首页
# driver.get("http://www.baidu.com")
# driver.find_element_by_xpath("//input[@id='su']")
# driver.find_element_by_id("su")
# driver.find_element_by_class_name("btn self-btn bg s_btn")  # 定位失败
# driver.find_element_by_link_text("百度一下")  # 定位失败
# driver.find_element_by_xpath("/html/body/div/div[2]/div[5]/div[1]/div/form/span[2]/input")
# time.sleep(3)
# driver.quit()

driver.get("http://www.baidu.com")  # 打开浏览器并访问该地址
driver.maximize_window()  # 是浏览器全屏
driver.set_window_size(100, 200)  # 设置浏览器窗口大小
driver.get_window_size()  # 获取浏览器窗口大小
driver.current_window_handle()  # 获取当前窗口的句柄
driver.window_handles()  # 获取所有窗口句柄
driver.refresh()  # 刷新当前页面
driver.forward()  # 当前页面前进
driver.back()  # 当前页面后退
driver.get_screenshot_as_file("xxx.png")  # 截图并保存
driver.get_cookie("cookieKey")  # 获取cookie信息
driver.add_cookie({'name': 'jl', 'value': '123123123'})  # 添加cookie
driver.delete_cookie("jl")  # 删除cookie
driver.switch_to.frame()  # 切换iframe
driver.switch_to.alert()  # 切换到警告弹窗
widows_handle = driver.current_window_handle  # 获取标签页句柄
driver.switch_to.window(widows_handle)  # 切换标签页
driver.close()  # 关闭当前页面
driver.quit()  # 关闭浏览器并退出驱动

driver.find_element_by_id("su").click()  # 点击元素
driver.find_element_by_id("kw").send_keys()  # 输入文本内容
driver.find_element_by_id("kw").clear()  # 清除文本框内容
driver.find_element_by_id("su").submit()  # 提交表单
driver.find_element_by_id("kw").is_displayed()  # 判断元素是否存在
driver.find_element_by_id("kw").is_selected()  # 判断元素是否已被勾选
driver.find_element_by_id("kw").is_enabled()  # 判断元素的可编辑状态
driver.find_element_by_id("kw").get_property("kw")  # 获取元素属性
driver.implicitly_wait(1)  # 智能等待元素出现
tag_name = driver.find_element_by_id("kw").tag_name  # 获取元素的名字
element_size = driver.find_element_by_id("kw").size  # 获取元素的宽和高
text = driver.find_element_by_id("su").text  # 获取元素的文本内容
location = driver.find_element_by_id("kw").location  # 获取当前元素的坐标



