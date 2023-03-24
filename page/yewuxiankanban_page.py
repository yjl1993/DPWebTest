#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/7 18:37
# @Author : jlyu
# @File : yewuxiankanban_page.py

from common import get_elements


class YWXKBPage:
    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def chanpinxian_douyin(self):
        """业务线看板-产品列表-抖音"""
        return self.get_elements.get_element("yewuxiankanban", "chanpinxian_douyin")

    def qushitu_shujushitu(self):
        """趋势图中的切换数据视图按钮"""
        return self.get_elements.get_element("yewuxiankanban", "qushitu_shujushitu")

    def shujushitu_jinshenliangziti(self):
        """趋势图-数据视图中的进审量字体"""
        return self.get_elements.get_element("yewuxiankanban", "shujushitu_jinshenliangziti")

    def jinshenliang_qushituzhibiao(self):
        """核心数据看板-进审量趋势图中的进审量指标字体"""
        return self.get_elements.get_element("yewuxiankanban", "jinshenliang_qushituzhibiao")

    def jinshenliang_shuju(self):
        """核心数据看板-进审量趋势图中的进审量指标数值"""
        return self.get_elements.get_element("yewuxiankanban", "jinshenliang_shuju")

    def shenchuliang_qushituzhibiao(self):
        """核心数据看板-审出量趋势图中的审出量指标字体"""
        return self.get_elements.get_element("yewuxiankanban", "shenchuliang_qushituzhibiao")

    def qushitushuju(self):
        """核心数据看板-审出量、平均审核延时v2、队列盲审一致率趋势图中的指标数值"""
        return self.get_elements.get_element("yewuxiankanban", "qushitushuju")

    def pingjunshenheyanshiv2_qushituzhibiao(self):
        """核心数据看板-平均审核延时v2趋势图中的指标字体"""
        return self.get_elements.get_element("yewuxiankanban", "pingjunshenheyanshiv2_qushituzhibiao")

    def duiliemangshenyizhilv_qushituzhibiao(self):
        """核心数据看板-队列盲审一致率趋势图中的指标字体"""
        return self.get_elements.get_element("yewuxiankanban", "duiliemangshenyizhilv_qushituzhibiao")

    def duilieshishitongji_jinshenliangziti(self):
        """队列实时统计中-表头中的"进审量"字体"""
        return self.get_elements.get_element("yewuxiankanban", "duilieshishitongji_jinshenliangziti")

    def duilieshishitongji_duiliesousuokuang(self):
        """队列实时统计-队列搜索框"""
        return self.get_elements.get_element("yewuxiankanban", "duilieshishitongji_duiliesousuokuang")

    def sousuokuang_shurukuang(self):
        """队列实时统计-队列搜索框-搜索输入框"""
        return self.get_elements.get_element("yewuxiankanban", "sousuokuang_shurukuang")

    def sousuokuangjieguodiyihang(self):
        """队列实时统计-队列搜索框-搜索框内的第一个搜索结果"""
        return self.get_elements.get_element("yewuxiankanban", "sousuokuangjieguodiyihang")

    def duilieshishitongji_zhibiaoleixing(self):
        """队列实时统计-指标类型"""
        return self.get_elements.get_element("yewuxiankanban", "duilieshishitongji_zhibiaoleixing")

    def duilieshishitongji_zhibiaoleixing_jiyashichangfenbu(self):
        """队列实时统计-指标类型-积压时长分布"""
        return self.get_elements.get_element("yewuxiankanban", "duilieshishitongji_zhibiaoleixing_jiyashichangfenbu")

    def jiyashichangfenbu_danqianshenhejiyazhibiao(self):
        """队列实时统计-指标类型-积压时长分布-表头中的"当前积压时长分布"字体"""
        return self.get_elements.get_element("yewuxiankanban", "jiyashichangfenbu_danqianshenhejiyazhibiao")

    def duilieshishitongji_diyihangjieguo(self):
        """队列实时统计表中的第一行数据结果显示"""
        return self.get_elements.get_element("yewuxiankanban", "duilieshishitongji_diyihangjieguo")

    def duilietongji_jinshenliangziti(self):
        """队列统计-重点指标-进审量字体"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_jinshenliangziti")

    def duilietongji_jieguodiyihang(self):
        """队列统计-表格中的第一行结果显示"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_jieguodiyihang")

    def duilietongji_duiliesousuokuang(self):
        """队列统计-队列搜索框"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_duiliesousuokuang")

    def duilietongjisousuo_shurukuang(self):
        """队列统计-队列搜索输入框"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongjisousuo_shurukuang")

    def duilietongji_zhibiaoleixing(self):
        """队列统计-指标类型"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_zhibiaoleixing")

    def zhibiaoleixing_xiaolvzhibiao(self):
        """队列统计-指标类型-效率指标"""
        return self.get_elements.get_element("yewuxiankanban", "zhibiaoleixing_xiaolvzhibiao")

    def xiaolvzhibiao_zaishenrenxiao(self):
        """队列统计-指标类型-效率指标-在审人效字体"""
        return self.get_elements.get_element("yewuxiankanban", "xiaolvzhibiao_zaishenrenxiao")

    def zhibiaoleixing_anquanzhibiao(self):
        """队列统计-指标类型-安全指标"""
        return self.get_elements.get_element("yewuxiankanban", "zhibiaoleixing_anquanzhibiao")

    def anquanzhibiao_monishiguziti(self):
        """队列统计-指标类型-安全指标-模拟事故字体"""
        return self.get_elements.get_element("yewuxiankanban", "anquanzhibiao_monishigu")

    def zhibiaoleixing_zhiliangzhibiao(self):
        """队列统计-指标类型-质量指标"""
        return self.get_elements.get_element("yewuxiankanban", "zhibiaoleixing_zhiliangzhibiao")

    def zhiliangzhibiao_mangshenzhibiao(self):
        """队列统计-指标类型-盲审指标字体"""
        return self.get_elements.get_element("yewuxiankanban", "zhiliangzhibiao_mangshenzhibiao")

    def zhibiaoleixing_shenchuzhibiao(self):
        """队列统计-指标类型-审出指标"""
        return self.get_elements.get_element("yewuxiankanban", "zhibiaoleixing_shenchuzhibiao")

    def duilietongji_sousuokuangjieguodiyihang(self):
        """队列统计-队列搜索框内的第一个搜索结果"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_sousuokuangjieguodiyihang")

    def qushitu_jinshenliangziyang(self):
        """队列统计-趋势图中的进审量字体"""
        return self.get_elements.get_element("yewuxiankanban", "qushitu_jinshenliangziyang")

    def duilietongji_gengduoshaixuan(self):
        """队列统计-页面缩小后出现的更多筛选按钮"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_gengduoshaixuan")

    def duilietongji_tongjifangshi(self):
        """队列统计-统计方式按钮"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_tongjifangshi")

    def duilietongji_huizongtongji(self):
        """队列统计-统计方式-汇总统计"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_huizongtongji")

    def duilietongji_shaixuanqi_yingyong(self):
        """队列统计-更多筛选-应用"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_shaixuanqi_yingyong")

    def duilietongji_huizongziti(self):
        """队列统计-汇总字体"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_huizongziti")

    def duilietongji_shijianlidu(self):
        """队列统计-时间粒度按钮"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_shijianlidu")

    def duilietongji_xiaoshiji(self):
        """队列统计-时间粒度-小时级"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_xiaoshiji")

    def shijianlidu_shijianxuanzekuang(self):
        """队列统计-时间粒度-开始时间选择框"""
        return self.get_elements.get_element("yewuxiankanban", "shijianlidu_shijianxuanzekuang")

    def shijianxuanze_zuijinqitian(self):
        """队列统计-时间粒度-最近7天按钮"""
        return self.get_elements.get_element("yewuxiankanban", "shijianxuanze_zuijinqitian")

    def duilietongji_qushitu(self):
        """队列统计-趋势图按钮"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_qushitu")

    def duilietongji_qushitu_jinshenliangziyang(self):
        """队列统计-趋势图中的进审量字体"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_qushitu_jinshenliangziyang")

    def duilietongji_qushitu_zhexianxianshi(self):
        """队列统计-趋势图中的折线图显示隐藏按钮"""
        return self.get_elements.get_element("yewuxiankanban", "duilietongji_qushitu_zhexianxianshi")

    # def (self):
    #     """"""
    #     return self.get_elements.get_element("yewuxiankanban", "")