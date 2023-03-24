#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/14 17:10
# @Author : jlyu
# @File : baidu_page.py

from common.get_elements import GetByMethods

class BaiduPage:

    def __init__(self, i):
        self.get_by_method = GetByMethods(i)

    def text(self):
        return self.get_by_method.get_element('send_text', 'baidu')

    def sumbit(self):
        return self.get_by_method.get_element('sumbit', 'baidu')
