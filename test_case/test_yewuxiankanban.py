#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/8 15:50
# @Author : jlyu
# @File : test_ywx_yewuxiankanban.py

import time
import allure

from test_case.sutup_case import SetUpCase
from page.yindaoye_page import YDYPage
from page.shujukeshihua_page import SJKSHPage
from page.yewuxiankanban_page import YWXKBPage
from selenium.webdriver.common.action_chains import ActionChains


class TestYWXKB:
    """业务线看板相关的用例"""

    def setup(self):
        setup_case = SetUpCase()
        self.driver = setup_case.setup_case()
        self.yindao_page = YDYPage(self.driver)
        self.shujukeshihua_page = SJKSHPage(self.driver)
        self.yewuxiankanban_page = YWXKBPage(self.driver)
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.guanfangkanban().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.yewuguanlixiang().click()
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.yewuxiankanban().click()
        self.driver.implicitly_wait(30)
        self.yewuxiankanban_page.chanpinxian_douyin().click()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    #  TODO 趋势图相关的case暂不可自动化，无法识别图片内的文字
    # @allure.title("ywx_1")
    # def test_ywx_1(self):
    #     """抖音业务线-核心数据-查看进审量趋势图;当前日期的柱形图中包含"进审量"字样，进审量大于0"""
    #     # self.yewuxiankanban_page.qushitu_shujushitu().click()
    #     # jinshenliang = self.yewuxiankanban_page.jinshenliang_qushituzhibiao()
    #     # ActionChains(self.driver).move_to_element(jinshenliang).perform()
    #     js = "var q=document.documentElement.scrollTop=50"
    #     self.driver.execute_script(js)
    #     text = self.yewuxiankanban_page.jinshenliang_qushituzhibiao().text
    #     assert text == "进审量"
    #     # value = self.yewuxiankanban_page.jinshenliang_shuju().text
    #     # assert int(value) > 0

    @allure.title("ywx_5")
    def test_ywx_5(self):
        """抖音业务线-队列实时统计-数据显示正常;列表表头中包含关键字“进审量”字样，列表第一行有数据显示"""
        text = self.yewuxiankanban_page.duilieshishitongji_jinshenliangziti().text
        assert text == "进审量"
        shuju = self.yewuxiankanban_page.duilieshishitongji_diyihangjieguo().text
        assert shuju is not None

    @allure.title("ywx_6")
    def test_ywx_6(self):
        """抖音业务线-队列实时统计-队列搜索关键字“中国”;搜索结果中列表第一行包含关键字“中国”"""
        time.sleep(1)
        self.yewuxiankanban_page.duilieshishitongji_duiliesousuokuang().click()
        time.sleep(1)
        self.yewuxiankanban_page.sousuokuang_shurukuang().send_keys("中国")
        time.sleep(1)
        self.yewuxiankanban_page.sousuokuangjieguodiyihang().click()
        time.sleep(1)
        text = self.yewuxiankanban_page.duilieshishitongji_diyihangjieguo().text
        assert "中国" in text

    @allure.title("ywx_7")
    def test_ywx_7(self):
        """抖音业务线-队列实时统计-切换指标类型为“积压时长分布”;列表表头中包含关键字“当前审核积压”字样，列表第一行有数据显示"""
        time.sleep(1)
        self.yewuxiankanban_page.duilieshishitongji_zhibiaoleixing().click()
        self.yewuxiankanban_page.duilieshishitongji_zhibiaoleixing_jiyashichangfenbu().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.jiyashichangfenbu_danqianshenhejiyazhibiao().text
        assert text == "当前审核积压"
        shuju = self.yewuxiankanban_page.duilieshishitongji_diyihangjieguo().text
        assert shuju is not None

    @allure.title("ywx_8")
    def test_ywx_8(self):
        """抖音业务线-队列统计-数据显示正常；列表表头中包含关键字“进审量”字样，列表第一行有数据显示"""
        text = self.yewuxiankanban_page.duilietongji_jinshenliangziti().text
        assert text == "进审量"
        value = self.yewuxiankanban_page.duilietongji_jieguodiyihang().text
        assert value is not None

    @allure.title("ywx_9")
    def test_ywx_9(self):
        """抖音业务线-队列统计-队列搜索关键字“中国;搜索结果中列表第一行包含关键字“中国””"""
        time.sleep(1)
        self.yewuxiankanban_page.duilietongji_duiliesousuokuang().click()
        self.yewuxiankanban_page.duilietongjisousuo_shurukuang().send_keys("中国")
        self.yewuxiankanban_page.duilietongji_sousuokuangjieguodiyihang().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.duilietongji_sousuokuangjieguodiyihang().text
        assert "中国" in text

    @allure.title("ywx_10")
    def test_ywx_10(self):
        """抖音业务线-队列统计-重点指标-切换统计方式为“汇总统计”;列表第一行结果中包含关键字“汇总”字样"""
        time.sleep(2)
        # self.yewuxiankanban_page.duilietongji_gengduoshaixuan().click()
        self.yewuxiankanban_page.duilietongji_tongjifangshi().click()
        self.driver.implicitly_wait(30)
        self.yewuxiankanban_page.duilietongji_huizongtongji().click()
        # self.driver.implicitly_wait(30)
        # self.yewuxiankanban_page.duilietongji_shaixuanqi_yingyong().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.duilietongji_huizongziti().text
        assert text == "汇总"

    @allure.title("ywx_11")
    def test_ywx_11(self):
        """抖音业务线-队列统计-重点指标-切换时间粒度为“小时级”;列表第一行有数据显示"""
        time.sleep(2)
        # self.yewuxiankanban_page.duilietongji_gengduoshaixuan().click()
        self.yewuxiankanban_page.duilietongji_shijianlidu().click()
        self.yewuxiankanban_page.duilietongji_xiaoshiji().click()
        # self.yewuxiankanban_page.duilietongji_shaixuanqi_yingyong().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.duilietongji_jieguodiyihang().text
        assert text is not None

    @allure.title("ywx_12")
    def test_ywx_12(self):
        """抖音业务线-队列统计-切换指标类型为“效率指标”；列表表头中包含关键字“在审人效(件/h)”字样，列表第一行有数据显示"""
        time.sleep(2)
        self.yewuxiankanban_page.duilietongji_zhibiaoleixing().click()
        self.yewuxiankanban_page.zhibiaoleixing_xiaolvzhibiao().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.xiaolvzhibiao_zaishenrenxiao().text
        assert text == "在审人效(件/h)"

    @allure.title("ywx_13")
    def test_ywx_13(self):
        """抖音业务线-队列统计-切换指标类型为“安全指标”;列表表头中包含关键字“模拟事故”字样，列表第一行有数据显示"""
        time.sleep(2)
        self.yewuxiankanban_page.duilietongji_zhibiaoleixing().click()
        self.yewuxiankanban_page.zhibiaoleixing_anquanzhibiao().click()
        self.driver.implicitly_wait(30)
        time.sleep(1)
        text = self.yewuxiankanban_page.xiaolvzhibiao_zaishenrenxiao().text
        assert "事故等级" in text
        self.driver.implicitly_wait(30)
        # self.yewuxiankanban_page.duilietongji_gengduoshaixuan().click()
        self.yewuxiankanban_page.duilietongji_shijianlidu().click()
        self.yewuxiankanban_page.shijianlidu_shijianxuanzekuang().click()
        self.yewuxiankanban_page.shijianxuanze_zuijinqitian().click()
        # self.yewuxiankanban_page.duilietongji_shaixuanqi_yingyong().click()
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.duilietongji_jieguodiyihang().text
        assert text is not None

    @allure.title("ywx_14")
    def test_ywx_14(self):
        """抖音业务线-队列统计-切换指标类型为“质量指标”;列表表头中包含关键字“盲审指标”字样，列表第一行有数据显示"""
        time.sleep(2)
        self.yewuxiankanban_page.duilietongji_zhibiaoleixing().click()
        self.yewuxiankanban_page.zhibiaoleixing_zhiliangzhibiao().click()
        self.driver.implicitly_wait(30)
        time.sleep(1)
        text = self.yewuxiankanban_page.zhiliangzhibiao_mangshenzhibiao().text
        assert "盲审指标" in text
        self.driver.implicitly_wait(30)
        text = self.yewuxiankanban_page.duilietongji_jieguodiyihang().text
        assert text is not None

    @allure.title("ywx_15")
    def test_ywx_15(self):
        """抖音业务线-队列统计-切换指标类型为“审出指标”;列表表头中包含关键字“自见率”字样，列表第一行有数据显示"""
        time.sleep(2)
        self.yewuxiankanban_page.duilietongji_zhibiaoleixing().click()
        self.yewuxiankanban_page.zhibiaoleixing_shenchuzhibiao().click()
        self.driver.implicitly_wait(30)
        time.sleep(1)
        text = self.yewuxiankanban_page.xiaolvzhibiao_zaishenrenxiao().text
        assert "自见率" in text
        # 目前审出指标无数据，先注释这一部分验证的代码
        # self.driver.implicitly_wait(30)
        # self.yewuxiankanban_page.duilietongji_gengduoshaixuan().click()
        # self.yewuxiankanban_page.duilietongji_shijianlidu().click()
        # self.yewuxiankanban_page.shijianlidu_shijianxuanzekuang().click()
        # self.yewuxiankanban_page.shijianxuanze_zuijinqitian().click()
        # self.yewuxiankanban_page.duilietongji_shaixuanqi_yingyong().click()
        # self.driver.implicitly_wait(30)
        # text = self.yewuxiankanban_page.duilietongji_jieguodiyihang().text
        # assert text is not None

    # @allure.title("ywx_16")
    # def test_ywx_16(self):
    #     """抖音业务线-队列统计-重点指标-切换至“趋势图”显示；页面中包含关键字“进审量”字样"""
    #     time.sleep(2)
    #     self.yewuxiankanban_page.duilietongji_qushitu().click()
    #     self.driver.implicitly_wait(30)
    #     time.sleep(10)
    #     self.yewuxiankanban_page.duilietongji_qushitu_zhexianxianshi().click()
    #     # text = self.yewuxiankanban_page.duilietongji_qushitu_jinshenliangziyang().text
    #     # assert text == "进审量"


    # @allure.title("ywx_")
    # def test_ywx_(self):
    #     """"""
    #
    # @allure.title("ywx_")
    # def test_ywx_(self):
    #     """"""
    #
    # @allure.title("ywx_")
    # def test_ywx_(self):
    #     """"""