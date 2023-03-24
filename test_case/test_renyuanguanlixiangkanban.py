#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/25 15:51
# @Author : jlyu
# @File : test_renyuanguanlixiangkanban.py

import time
import allure

from test_case.sutup_case import SetUpCase
from page.yindaoye_page import YDYPage
from page.shujukeshihua_page import SJKSHPage
from page.renyuanguanlixiangkanban_page import RYGLXKBPage


class TestRYGLX:
    """人员管理向看板相关的用例"""

    def setup(self):
        setup_case = SetUpCase()
        self.driver = setup_case.setup_case()
        self.yindao_page = YDYPage(self.driver)
        self.shujukeshihua_page = SJKSHPage(self.driver)
        self.renyuanguanlixiangkanban_page = RYGLXKBPage(self.driver)
        self.driver.implicitly_wait(30)
        self.shujukeshihua_page.guanfangkanban().click()
        self.driver.implicitly_wait(30)
        #  点击人员管理向看板
        self.shujukeshihua_page.renyuanguanlixiangkanban().click()
        self.driver.implicitly_wait(30)
        # 进入cqc内容审核看板
        self.renyuanguanlixiangkanban_page.jinrukanban().click()
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    @allure.title("ryglx_1")
    def test_ryglxx_1(self):
        """判断CQC内容审核部门页面加载打开正常；页面打开正常无报错，该页面包含”CQC内容审核“字样"""
        text = self.renyuanguanlixiangkanban_page.CQCneirongshenhe().text
        assert text == "CQC内容审核"

    @allure.title("ryglx_2")
    def test_ryglx_2(self):
        """顶部筛选栏切换部门，只选择”天津基地“;部门切换正常，该页面包含”天津基地“字样"""
        self.renyuanguanlixiangkanban_page.cqcbumen().click()
        self.renyuanguanlixiangkanban_page.cqcbumen_list().click()
        self.renyuanguanlixiangkanban_page.cqcbumen_search().send_keys("天津基地")
        self.driver.implicitly_wait(30)
        self.renyuanguanlixiangkanban_page.tianjinjidi_button().click()
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.tianjin_text().text
        assert text == "天津基地"

    @allure.title("ryglx_3")
    def test_ryglx_3(self):
        """顶部筛选栏切换时间粒度由”小时级“切换至”天级级“；时间粒度切换正常，当前筛选项为”天级“"""
        self.renyuanguanlixiangkanban_page.shijianlidu().click()
        self.renyuanguanlixiangkanban_page.shijianlidu_tianji().click()
        text = self.renyuanguanlixiangkanban_page.danqianshijianlidu().text
        assert text == "天级"

    @allure.title("ryglx_4")
    def test_ryglx_4(self):
        """顶部筛选栏切换指标类型，由”重点指标“切换至”工时指标“；指标切换正常，当前页面包含”班次内任务量“字样"""
        self.renyuanguanlixiangkanban_page.zhibiaoleixing().click()
        self.renyuanguanlixiangkanban_page.zhibiaoleixing_gongshizhibiao().click()
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.bancineirenwuliang().text
        assert text == "班次内任务量"

    @allure.title("ryglx_5")
    def test_ryglx_5(self):
        """审核员统计-审核榜-搜索框搜索关键字”zhang“；正常返回搜索结果，结果中包含关键字”zhang“"""
        self.renyuanguanlixiangkanban_page.shenhebang_sousuokuang().send_keys("zhang")
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.shenhebang_diyilan().text
        assert "zhang" in text

    @allure.title("ryglx_6")
    def test_ryglx_6(self):
        """审核员统计-分维度对比-分队列-搜索框搜索”中国“;第一行结果中包含关键字”中国“"""
        self.renyuanguanlixiangkanban_page.fenweiduduibi_sousuokuang().send_keys("中国")
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.fenweiduduibi_diyihangjieguo().text
        assert "中国" in text

    @allure.title("ryglx_7")
    def test_ryglx_7(self):
        """1、审核员统计-分维度对比-切换聚合方式至”分内容类型“ 2、搜索框搜索关键字”图文“；第一行结果中包含关键字”图文“"""
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi().click()
        time.sleep(1)
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi_fenneirong().click()
        self.renyuanguanlixiangkanban_page.fenweiduduibi_sousuokuang().send_keys("图文")
        self.driver.implicitly_wait(30)
        time.sleep(10)
        text = self.renyuanguanlixiangkanban_page.fenweiduduibi_diyihangjieguo().text
        assert "图文" in text

    @allure.title("ryglx_8")
    def test_ryglx_8(self):
        """1、审核员统计-分维度对比-切换聚合方式至”分队列类型“ 2、搜索框搜索关键字”召回“;第一行结果中包含关键字”召回“"""
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi().click()
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi_fenduilei().click()
        self.renyuanguanlixiangkanban_page.fenweiduduibi_sousuokuang().send_keys("召回")
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.fenweiduduibi_diyihangjieguo().text
        assert "召回" in text

    @allure.title("ryglx_9")
    def test_ryglx_9(self):
        """1、审核员统计-分维度对比-切换聚合方式至”分工作城市“ 2、搜索框搜索关键字”Tianjin";第一行结果中包含关键字”Tianjin“"""
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi().click()
        self.renyuanguanlixiangkanban_page.fenweiduduibi_juhefangshi_fengongzuochengshi().click()
        self.renyuanguanlixiangkanban_page.fenweiduduibi_sousuokuang().send_keys("Tianjin")
        self.driver.implicitly_wait(30)
        text = self.renyuanguanlixiangkanban_page.fenweiduduibi_diyihangjieguo().text
        assert "Tianjin" in text

    @allure.title("ryglx_10")
    def test_ryglx_10(self):
        """1、页面由“审核员统计”切换至“部门全指标统计” 2、切换分布对比的指标名称，由”审核量“切换至”在审人效(件/h)“"""
        self.renyuanguanlixiangkanban_page.bumenquanzhibiaotongji().click()
        self.renyuanguanlixiangkanban_page.fengbuduibi_zhibiaomingcheng().click()
        self.renyuanguanlixiangkanban_page.zhibiaomingcheng_zaishenrenxiaoxuanxian().click()
        text = self.renyuanguanlixiangkanban_page.zhibiaomingcheng_zaishenrenxiao().text
        assert text == "在审人效(件/h)"


    #@allure.title("ryglx_")
    # def test_ryglx_(self):
    #     """"""

    #@allure.title("ryglx_")
    # def test_ryglx_(self):
    #     """"""
    #
    #@allure.title("ryglx_")
    # def test_ryglx_(self):
    #     """"""


