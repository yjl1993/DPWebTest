#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/26 10:47
# @Author : jlyu
# @File : renyuanguanlixiangkanban_page.py

from common import get_elements


class RYGLXKBPage:
    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def liebiao_CQCneirongshenhe(self):
        """部门列表中的CQC内容审核按钮"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "liebiao_CQCneirongshenhe")

    def jinrukanban(self):
        """进入CQC内容审核的按钮"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "jinrukanban")

    def CQCneirongshenhe(self):
        """CQC内容审核 字样"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "CQCneirongshenhe")

    def cqcbumen(self):
        """CQC内容审核页面中的部门筛选按钮"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "cqcbumen")

    def cqcbumen_list(self):
        """部门筛选列表"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "cqcbumen_list")

    def cqcbumen_search(self):
        """部门搜索框"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "cqcbumen_search")

    def tianjinjidi_button(self):
        """部门筛选项-天津"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "tianjinjidi_button")

    def tianjin_text(self):
        """用于判断部门筛选项中选中了天津基地"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "tianjin_text")

    def shijianlidu(self):
        """底部筛选栏-时间粒度"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "shijianlidu")

    def shijianlidu_tianji(self):
        """时间粒度-天级选项"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "shijianlidu_tianji")

    def shujianludu_xiaoshiji(self):
        """时间粒度-小时级选项"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "shujianludu_xiaoshiji")

    def danqianshijianlidu(self):
        """时间粒度筛选器当前选择的时间粒度"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "danqianshijianlidu")

    def zhibiaoleixing(self):
        """筛选栏-指标类型"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "zhibiaoleixing")

    def zhibiaoleixing_gongshizhibiao(self):
        """指标类型-工时指标"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "zhibiaoleixing_gongshizhibiao")

    def bancineirenwuliang(self):
        """工时指标页面中的班次内任务量，用于判断当前页面为工时指标页面"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "bancineirenwuliang")

    def shenhebang_sousuokuang(self):
        """审核员统计-审核榜-审核员搜索框"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "shenhebang_sousuokuang")

    def shenhebang_diyilan(self):
        """审核榜-搜索结果中显示在第一位的审核员"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "shenhebang_diyilan")

    def fenweiduduibi_juhefangshi(self):
        """分维度对比-聚合方式选择框"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_juhefangshi")

    def fenweiduduibi_diyihangjieguo(self):
        """分维度对比-搜索结果中显示在第一行的位置"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_diyihangjieguo")

    def fenweiduduibi_juhefangshi_fenneirong(self):
        """分维度对比-聚合方式-分内容类型"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_juhefangshi_fenneirong")

    def fenweiduduibi_juhefangshi_fenduilei(self):
        """分维度对比-聚合方式-分队列类型"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_juhefangshi_fenduilei")

    def fenweiduduibi_juhefangshi_fengongzuochengshi(self):
        """分工作城市"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_juhefangshi_fengongzuochengshi")

    def fenweiduduibi_sousuokuang(self):
        """分维度对比-聚合维度搜索框"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fenweiduduibi_sousuokuang")

    def bumenquanzhibiaotongji(self):
        """部门全指标统计tab按钮"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "bumenquanzhibiaotongji")

    def fengbuduibi_zhibiaomingcheng(self):
        """分布对比中的指标名称框"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "fengbuduibi_zhibiaomingcheng")

    def zhibiaomingcheng_zaishenrenxiaoxuanxian(self):
        """指标名称框中的"在审人效（件/h）选项"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "zhibiaomingcheng_zaishenrenxiaoxuanxian")

    def zhibiaomingcheng_zaishenrenxiao(self):
        """用于判断当前指标名称选择的是在审人效这个筛选项"""
        return self.get_elements.get_element("renyuanguanlixiangkanban", "zhibiaomingcheng_zaishenrenxiao")

    # def (self):
    #     """"""
    #     return self.get_elements.get_element("renyuanguanlixiangkanban", "")
    #
    # def (self):
    #     """"""
    #     return self.get_elements.get_element("renyuanguanlixiangkanban", "")
    #
    # def (self):
    #     """"""
    #     return self.get_elements.get_element("renyuanguanlixiangkanban", "")