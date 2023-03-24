#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/26 11:18
# @Author : jlyu
# @File : shujukeshihua_page.py

from common import get_elements

class SJKSHPage:

    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def guanfangkanban(self):
        '''官方看板'''
        return self.get_elements.get_element("shujukeshihua", "guanfangkanban")

    def woguanzhude(self):
        '''我关注的'''
        return self.get_elements.get_element("shujukeshihua", "woguanzhude")

    def renyuanguanlixiangkanban(self):
        '''人员管理向看板'''
        return self.get_elements.get_element("shujukeshihua", "renyuanguanlixiangkanban")

    def yewuguanlixiang(self):
        '''业务管理向看板'''
        return self.get_elements.get_element("shujukeshihua", "yewuguanlixiang")

    def yewuxiankanban(self):
        '''业务线看板'''
        return self.get_elements.get_element("shujukeshihua", "yewuxiankanban")

    def douyinjuhekanban(self):
        '''抖音聚合看板'''
        return self.get_elements.get_element("shujukeshihua", "douyinjuhekanban")

    def duiliejuhekanban(self):
        '''队列聚合看板'''
        return self.get_elements.get_element("shujukeshihua", "duiliejuhekanban")

    # def (self):
    #     return self.get_elements.get_element("")
    #
    # def (self):
    #     return self.get_elements.get_element("")
    #
    # def (self):
    #     return self.get_elements.get_element("")
    #
    # def (self):
    #     return self.get_elements.get_element("")