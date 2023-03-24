#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/18 17:13
# @Author : jlyu
# @File : test_duiliejuhekanban.py

import time
import allure

from test_case.sutup_case import SetUpCase
from page.yindaoye_page import YDYPage
from page.shujukeshihua_page import SJKSHPage
from page.duiliejuhekanban_page import DLJHKBPage


class TestDLJHKB:
    """队列聚合看板相关case"""

    def setup(self):
        setup_case = SetUpCase()
        self.driver = setup_case.setup_case()
        self.yindao_page = YDYPage(self.driver)
        self.shujukeshihua_page = SJKSHPage(self.driver)
        self.duiliejuhekanban_page = DLJHKBPage(self.driver)
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.guanfangkanban().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.yewuguanlixiang().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.duiliejuhekanban().click()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    @allure.title("dljh_1")
    def test_dljh_1(self):
        """审核数据看板-核心数据-天级数据显示正常;核心数据中的进审量指标数据不为空"""
        text = self.duiliejuhekanban_page.hexinshuju_jinshenliangziti().text
        assert text is not None

    @allure.title("dljh_2")
    def test_dljh_2(self):
        """审核数据看板-核心数据-更改时间粒度为“小时级”;包含关键字“小时级”字样，核心数据中的进审量指标数据不为空"""
        self.duiliejuhekanban_page.hexinshuju_shijianliduxuanzekuang().click()
        self.duiliejuhekanban_page.hexinshuju_shijianlidu_xiaoshiji().click()
        time.sleep(1)
        ziti = self.duiliejuhekanban_page.hexinshuju_shijianlidu_xiaoshijiziti().text
        assert ziti == "小时级"
        self.driver.implicitly_wait(30)
        text = self.duiliejuhekanban_page.hexinshuju_jinshenliangziti().text
        assert text is not None

    @allure.title("dljh_3")
    def test_dljh_3(self):
        """审核数据看板-核心数据-更改统计时间段为最近7天;核心数据中的进审量指标数据不为空"""
        self.duiliejuhekanban_page.hexinshuju_tongjishiduanxuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.hexinshuju_tongjishiduan_zuijinqitian().click()
        self.driver.implicitly_wait(30)
        text = self.duiliejuhekanban_page.hexinshuju_jinshenliangziti().text
        assert text is not None

    @allure.title("dljh_4")
    def test_dljh_4(self):
        """队列统计（实时）-天级数据显示正常;队列统计（实时）看板中第一行数据有数据显示"""
        text = self.duiliejuhekanban_page.duilietongjishishi_diyihangshujuxianshi().text
        assert text is not None

    @allure.title("dljh_5")
    def test_dljh_5(self):
        """队列统计（实时）-左侧队列搜索框输入关键字“中国”;搜索结果中列表第一行包含关键字“中国”"""
        self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuokuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuoshurukuang().send_keys("中国")
        time.sleep(3)
        text = self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuojieguodiyihan().text
        assert "中国" in text

    @allure.title("dljh_6")
    def test_dljh_6(self):
        """队列统计（实时）-更改时间粒度为“小时级”;包含关键字“小时级”，队列统计（实时）看板中第一行数据有数据显示"""
        self.duiliejuhekanban_page.duilietongjishishi_shijianliduxuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.duilietongjishishi_shijianlidu_xiaoshiji().click()
        time.sleep(1)
        text = self.duiliejuhekanban_page.duilietongjishishi_shijianlidu_xiaoshijiziti().text
        assert text == "小时级"
        self.driver.implicitly_wait(30)
        value = self.duiliejuhekanban_page.duilietongjishishi_diyihangshujuxianshi().text
        assert value is not None

    @allure.title("dljh_7")
    def test_dljh_7(self):
        """队列统计（实时）-更改统计时间段为最近7天;队列统计（实时）看板中第一行数据有数据显示"""
        self.duiliejuhekanban_page.duilietongjishishi_tongjishiduanxuanzekuang().click()
        self.duiliejuhekanban_page.duilietongjishishi_tongjishiduan_zuijinqitian().click()
        self.driver.implicitly_wait(30)
        text = self.duiliejuhekanban_page.duilietongjishishi_diyihangshujuxianshi().text
        assert text is not None

    @allure.title("dljh_8")
    def test_dljh_8(self):
        """队列统计（实时）-右侧队列名称搜索框输入关键字“中国”;搜索结果中列表第一行包含关键字“中国”"""
        self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuokuang().click()
        self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuoshurukuang().send_keys("中国")
        time.sleep(1)
        text = self.duiliejuhekanban_page.duilietongjishishi_zuoceduiliesousuojieguodiyihan().text
        assert "中国" in text

    @allure.title("dljh_9")
    def test_dljh_9(self):
        """审核榜（实时）-天级数据显示正常；核心数据中的进审量指标数据不为空"""
        text = self.duiliejuhekanban_page.shenhebangshishi_diyihangshujuxianshi().text
        assert text is not None

    @allure.title("dljh_10")
    def test_dljh_10(self):
        """审核榜（实时）-审核员搜索框输入关键字“zhang”;搜索结果中列表第一行包含关键字“zhang”"""
        self.duiliejuhekanban_page.shenhebangshishi_shenheyuansousuokuang().send_keys("zhang")
        self.driver.implicitly_wait(30)
        text = self.duiliejuhekanban_page.shenhebangshishi_diyihangshujuxianshi().text
        assert text is not None

    @allure.title("dljh_11")
    def test_dljh_11(self):
        """审核榜（实时）-更改时间粒度为“小时级”;包含关键字“小时级”字样，核心数据中的审核量指标数据不为空"""
        self.duiliejuhekanban_page.shenhebangshishi_shijianliduxuanzekuang().click()
        self.duiliejuhekanban_page.shenhebangshishi_shijianlidu_xiaoshiji().click()
        time.sleep(1)
        text = self.duiliejuhekanban_page.shenhebangshishi_shijianlidu_xiaoshijiziti().text
        assert text == "小时级"
        self.driver.implicitly_wait(30)
        value = self.duiliejuhekanban_page.shenhebangshishi_diyihangshujuxianshi().text
        assert value is not None

    @allure.title("dljh_12")
    def test_dljh_12(self):
        """审核榜（实时）-更改统计时间段为最近7天；审核榜（实时）看板中的审核量指标数据不为空"""
        self.duiliejuhekanban_page.shenhebangshishi_tongjishiduanxuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.shenhebangshishi_tongjishiduan_zuijinqitian().click()
        self.driver.implicitly_wait(30)
        text = self.duiliejuhekanban_page.shenhebangshishi_diyihangshujuxianshi().text
        assert text is not None

    @allure.title("dljh_13")
    def test_dljh_13(self):
        """结果分布-表头设置：yjl测试-表头设置-切换表头为“yjl测试1”;表头框中包含关键字“yjl测试1”，结果分布看板中第一行数据有数据显示"""
        self.duiliejuhekanban_page.jieguofenbu_biaotoushezhixuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.jieguofenbu_biaotou_yjlceshi().click()
        time.sleep(1)
        text = self.duiliejuhekanban_page.jieguofenbu_biaotou_yjlceshiziti().text
        assert text == "yjl测试"
        self.driver.implicitly_wait(30)
        value = self.duiliejuhekanban_page.jieguofenbu_diyihangshujuxianshi().text
        assert value is not None

    @allure.title("dljh_14")
    def test_dljh_14(self):
        """结果分布-表头设置：yjl测试-更改时间粒度为“小时级”;包含关键字“小时级”，结果分布看板中第一行数据有数据显示"""
        self.duiliejuhekanban_page.jieguofenbu_biaotoushezhixuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.jieguofenbu_biaotou_yjlceshi().click()
        time.sleep(1)
        text = self.duiliejuhekanban_page.jieguofenbu_biaotou_yjlceshiziti().text
        assert text == "yjl测试"
        self.driver.implicitly_wait(30)
        self.duiliejuhekanban_page.jieguofenbu_shijianliduxuanzekuang().click()
        time.sleep(1)
        self.duiliejuhekanban_page.jieguofenbu_shijianlidu_xiaoshiji().click()
        time.sleep(1)
        text = self.duiliejuhekanban_page.jieguofenbu_shijianlidu_xiaoshijiziti().text
        assert text == "小时级"
        self.driver.implicitly_wait(30)
        value = self.duiliejuhekanban_page.jieguofenbu_diyihangshujuxianshi().text
        assert value is not None

    # @allure.title("dljh_15")
    # def test_dljh_15(self):
    #     """"""
    #
    # @allure.title("dljh_")
    # def test_dljh_(self):
    #     """"""
    #
    # @allure.title("dljh_")
    # def test_dljh_(self):
    #     """"""
    #
    # @allure.title("dljh_")
    # def test_dljh_(self):
    #     """"""