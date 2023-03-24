#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/10 19:46
# @Author : jlyu
# @File : douyinjuhekanban_page.py

from common import get_elements


class DYJHPage:
    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def pingjunyanshiziti(self):
        """时段内平均延时（min）字体"""
        return self.get_elements.get_element("douyinjuhekanban", "pingjunyanshiziti")

    def zaishenrenshuziti(self):
        """在审人数字体"""
        return self.get_elements.get_element("douyinjuhekanban", "zaishenrenshuziti")

    def duiliexiangqing(self):
        """队列详情按钮"""
        return self.get_elements.get_element("douyinjuhekanban", "duiliexiangqing")

    def jinrileijishuju(self):
        """今日累计数据"""
        return self.get_elements.get_element("douyinjuhekanban", "jinrileijishuju")

    def duiliebiaotiziti(self):
        """队列详情内的队列标题字体"""
        return self.get_elements.get_element("douyinjuhekanban", "duiliebiaotiziti")

    def duiliexiangqingdiyihangshuju(self):
        """队列详情页第一行数据"""
        return self.get_elements.get_element("douyinjuhekanban", "duiliexiangqingdiyihangshuju")

    def jin20fenzhongshuju(self):
        """近20分钟数据"""
        return self.get_elements.get_element("douyinjuhekanban", "jin20fenzhongshuju")

    def diyihangdierliekapian_zhidinganniu(self):
        """第一行第二列卡片的置顶按钮"""
        return self.get_elements.get_element("douyinjuhekanban", "diyihangdierliekapian_zhidinganniu")

    def diyihangdiyilie_duiliemingcheng(self):
        """第一行第一列卡片的队列名称"""
        return self.get_elements.get_element("douyinjuhekanban", "diyihangdiyilie_duiliemingcheng")

    def diyihangdierlie_duiliemingcheng(self):
        """第一行第二列卡片的队列名称"""
        return self.get_elements.get_element("douyinjuhekanban", "diyihangdierlie_duiliemingcheng")

    # def (self):
    #     """"""
    #     return self.get_elements.get_element("douyinjuhekanban", "")
    #
    # def (self):
    #     """"""
    #     return self.get_elements.get_element("douyinjuhekanban", "")
    #
    # def (self):
    #     """"""
    #     return self.get_elements.get_element("douyinjuhekanban", "")
    #
    # def (self):
    #     """"""
    #     return self.get_elements.get_element("douyinjuhekanban", "")