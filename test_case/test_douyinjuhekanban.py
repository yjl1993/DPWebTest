#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/10 19:49
# @Author : jlyu
# @File : test_douyinjuhekanban.py

import time
import allure

from test_case.sutup_case import SetUpCase
from page.yindaoye_page import YDYPage
from page.shujukeshihua_page import SJKSHPage
from page.douyinjuhekanban_page import DYJHPage


class TestDYJH:
    """抖音聚合看板相关case"""

    def setup(self):
        setup_case = SetUpCase()
        self.driver = setup_case.setup_case()
        self.yindao_page = YDYPage(self.driver)
        self.shujukeshihua_page = SJKSHPage(self.driver)
        self.douyuinjuhe_page = DYJHPage(self.driver)
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.guanfangkanban().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.yewuguanlixiang().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.douyinjuhekanban().click()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    @allure.title("dyjh_1")
    def test_dyjh_1(self):
        """队列卡片显示正常;卡片中审核数据的“时段内平均延时”指标数据不为空，人力数据的“在审人数”指标数据不为空"""
        text = self.douyuinjuhe_page.pingjunyanshiziti().text
        assert text is not None
        text1 = self.douyuinjuhe_page.zaishenrenshuziti().text
        assert text1 is not None

    @allure.title("dyjh_2")
    def test_dyjh_2(self):
        """队列卡片详情数据-今日累计数据表显示正常;详情表中包含“队列标题”字样，表中第一行有数据显示"""
        self.douyuinjuhe_page.duiliexiangqing().click()
        text = self.douyuinjuhe_page.duiliebiaotiziti().text
        assert text == "队列标题"
        value = self.douyuinjuhe_page.duiliexiangqingdiyihangshuju().text
        assert value is not None

    @allure.title("dyjh_3")
    def test_dyjh_3(self):
        """队列卡片详情数据-近20分钟数据表显示正常;详情表中包含“队列标题”字样，表中第一行有数据显示"""
        self.douyuinjuhe_page.duiliexiangqing().click()
        self.douyuinjuhe_page.jin20fenzhongshuju().click()
        text = self.douyuinjuhe_page.duiliebiaotiziti().text
        assert text == "队列标题"
        vaule = self.douyuinjuhe_page.duiliexiangqingdiyihangshuju().text
        assert vaule is not None

    #  TODO 置顶按钮暂不可点击，放到后面实现
    # @allure.title("dyjh_4")
    # def test_dyjh_4(self):
    #     """置顶第一行第二列队列卡片A;置顶后队列卡片A出现在第一行第一列"""
    #     text = self.douyuinjuhe_page.diyihangdierlie_duiliemingcheng().text
    #     time.sleep(20)
    #     self.douyuinjuhe_page.diyihangdierliekapian_zhidinganniu().click()
    #     time.sleep(10)
    #     text1 = self.douyuinjuhe_page.diyihangdiyilie_duiliemingcheng().text
    #     assert text == text1
    #     time.sleep(10)

    @allure.title("dyjh_")
    def test_dyjh_(self):
        """"""

    @allure.title("dyjh_")
    def test_dyjh_(self):
        """"""

    @allure.title("dyjh_")
    def test_dyjh_(self):
        """"""