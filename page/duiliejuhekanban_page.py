#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/2/18 16:46
# @Author : jlyu
# @File : duiliejuhekanban_page.py

from common import get_elements


class DLJHKBPage:
    def __init__(self, i):
        self.get_elements = get_elements.GetByMethods(i)

    def hexinshuju_jinshenliangziti(self):
        """核心数据（实时）-进审量字体"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_jinshenliangziti")

    def hexinshuju_shijianliduxuanzekuang(self):
        """核心数据（实时）-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_shijianliduxuanzekuang")

    def hexinshuju_shijianlidu_xiaoshiji(self):
        """核心数据（实时）-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_shijianlidu_xiaoshiji")

    def hexinshuju_shijianlidu_xiaoshijiziti(self):
        """核心数据（实时）-时间粒度-小时级字体"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_shijianlidu_xiaoshijiziti")

    def hexinshuju_tongjishiduanxuanzekuang(self):
        """核心数据（实时）-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_tongjishiduanxuanzekuang")

    def hexinshuju_tongjishiduan_zuijinqitian(self):
        """核心数据（实时）-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "hexinshuju_tongjishiduan_zuijinqitian")

    def duilietongjishishi_diyihangshujuxianshi(self):
        """队列统计（实时）-第一行数据显示"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_diyihangshujuxianshi")

    def duilietongjishishi_zuoceduiliesousuokuang(self):
        """队列统计（实时）-左侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_zuoceduiliesousuokuang")

    def duilietongjishishi_zuoceduiliesousuoshurukuang(self):
        """队列统计（实时）-左侧队列搜索输入框"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_zuoceduiliesousuoshurukuang")

    def duilietongjishishi_zuoceduiliesousuojieguodiyihan(self):
        """队列统计（实时）-左侧队列搜索结果第一行结果显示"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_zuoceduiliesousuojieguodiyihan")

    def duilietongjishishi_shijianliduxuanzekuang(self):
        """队列统计（实时）-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_shijianliduxuanzekuang")

    def duilietongjishishi_shijianlidu_xiaoshiji(self):
        """队列统计（实时）-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_shijianlidu_xiaoshiji")

    def duilietongjishishi_shijianlidu_xiaoshijiziti(self):
        """队列统计（实时）-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_shijianlidu_xiaoshijiziti")

    def duilietongjishishi_tongjishiduanxuanzekuang(self):
        """队列统计（实时）-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_tongjishiduanxuanzekuang")

    def duilietongjishishi_tongjishiduan_zuijinqitian(self):
        """队列统计（实时）-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_tongjishiduan_zuijinqitian")

    def duilietongjishishi_youceduiliesousuokuang(self):
        """队列统计（实时）-右侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "duilietongjishishi_youceduiliesousuokuang")

    def shenhebangshishi_diyihangshujuxianshi(self):
        """审核榜（实时）-第一行数据显示"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_diyihangshujuxianshi")

    def shenhebangshishi_shenheyuansousuokuang(self):
        """审核榜（实时）-审核员搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_shenheyuansousuokuang")

    def shenhebangshishi_shijianliduxuanzekuang(self):
        """审核榜（实时）-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_shijianliduxuanzekuang")

    def shenhebangshishi_shijianlidu_xiaoshiji(self):
        """审核榜（实时）-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_shijianlidu_xiaoshiji")

    def shenhebangshishi_shijianlidu_xiaoshijiziti(self):
        """审核榜（实时）-时间粒度-小时级字体"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_shijianlidu_xiaoshijiziti")

    def shenhebangshishi_tongjishiduanxuanzekuang(self):
        """审核榜（实时）-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_tongjishiduanxuanzekuang")

    def shenhebangshishi_tongjishiduan_zuijinqitian(self):
        """审核榜（实时）-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "shenhebangshishi_tongjishiduan_zuijinqitian")

    def jieguofenbu_biaotoushezhixuanzekuang(self):
        """结果分布-表头设置"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_biaotoushezhixuanzekuang")

    def jieguofenbu_biaotou_yjlceshi(self):
        """结果分布-表头设置-yjl测试"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_biaotou_yjlceshi")

    def jieguofenbu_biaotou_yjlceshiziti(self):
        """结果分布-表头设置-yjl测试字体"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_biaotou_yjlceshiziti")

    def jieguofenbu_diyihangshujuxianshi(self):
        """结果分布-第一行数据显示"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_diyihangshujuxianshi")

    def jieguofenbu_shijianliduxuanzekuang(self):
        """结果分布-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_shijianliduxuanzekuang")

    def jieguofenbu_shijianlidu_xiaoshiji(self):
        """结果分布-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_shijianlidu_xiaoshiji")

    def jieguofenbu_shijianlidu_xiaoshijiziti(self):
        """结果分布-时间粒度-小时级字体"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_shijianlidu_xiaoshijiziti")

    def jieguofenbu_tongjishiduanxuanzekuang(self):
        """结果分布-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_tongjishiduanxuanzekuang")

    def jieguofenbu_tongjishiduan_zuijinqitian(self):
        """结果分布-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_tongjishiduan_zuijinqitian")

    def jieguofenbu_youceduiliesousuokuang(self):
        """结果分布-右侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "jieguofenbu_youceduiliesousuokuang")

    def choujianshuju_choujianhegelvtongji_diyihangshujuxianshi(self):
        """抽检数据-抽检合格率统计-第一行数据显示"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_diyihangshujuxianshi")

    def choujianshuju_choujianhegelvtongji_zuoceduiliesousuokuang(self):
        """抽检数据-抽检合格率统计-左侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_zuoceduiliesousuokuang")

    def choujianshuju_choujianhegelvtongji_zuoceduiliesousuoshurukuang(self):
        """抽检数据-抽检合格率统计-左侧队列搜索输入框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_zuoceduiliesousuoshurukuang")

    def choujianshuju_choujianhegelvtongji_shijianliduxuanzekuang(self):
        """抽检数据-抽检合格率统计-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shijianliduxuanzekuang")

    def choujianshuju_choujianhegelvtongji_shijianlidu_xiaoshiji(self):
        """抽检数据-抽检合格率统计-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shijianlidu_xiaoshiji")

    def choujianshuju_choujianhegelvtongji_tongjishijianxuanzekuang(self):
        """抽检数据-抽检合格率统计-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_tongjishijianxuanzekuang")

    def choujianshuju_choujianhegelvtongji_tongjishiduan_zuijinqitian(self):
        """抽检数据-抽检合格率统计-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_tongjishiduan_zuijinqitian")

    def choujianshuju_choujianhegelvtongji_youceduiliesousuokuang(self):
        """抽检数据-抽检合格率统计-右侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_youceduiliesousuokuang")

    def choujianshuju_choujianhegelvtongji_shenheyuan_diyihangshujuxianshi(self):
        """抽检数据-抽检合格率统计（审核员）-第一行数据显示"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_diyihangshujuxianshi")

    def choujianshuju_choujianhegelvtongji_shenheyuan_zuoceduiliesousuokuang(self):
        """抽检数据-抽检合格率统计（审核员）-左侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_zuoceduiliesousuokuang")

    def choujianshuju_choujianhegelvtongji_shenheyuan_zuoceduiliesousuoshurukuang(self):
        """抽检数据-抽检合格率统计（审核员）-左侧队列搜索输入框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_zuoceduiliesousuoshurukuang")

    def choujianshuju_choujianhegelvtongji_shenheyuan_shijianliduxuanzekuang(self):
        """抽检数据-抽检合格率统计（审核员）-时间粒度选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_shijianliduxuanzekuang")

    def choujianshuju_choujianhegelvtongji_shenheyuan_shijianlidu_xiaoshiji(self):
        """抽检数据-抽检合格率统计（审核员）-时间粒度-小时级"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_shijianlidu_xiaoshiji")

    def choujianshuju_choujianhegelvtongji_shenheyuan_tongjishiduanxuanzekuang(self):
        """抽检数据-抽检合格率统计（审核员）-统计时段选择框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_tongjishiduanxuanzekuang")

    def choujianshuju_choujianhegelvtongji_shenheyuan_tongjishiduan_zuijinqitian(self):
        """抽检数据-抽检合格率统计（审核员）-统计时段-最近七天"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_tongjishiduan_zuijinqitian")

    def choujianshuju_choujianhegelvtongji_shenheyuan_youceduiliesousuokuang(self):
        """抽检数据-抽检合格率统计（审核员）-右侧队列搜索框"""
        return self.get_elements.get_element("duiliejuhekaban", "choujianshuju_choujianhegelvtongji_shenheyuan_youceduiliesousuokuang")

    # def (self):
    #     """抽检数据-抽检合格率统计（审核员）-"""
    #     return self.get_elements.get_element("duiliejuhekaban", "")
    #
    # def (self):
    #     """抽检数据-抽检合格率统计（审核员）-"""
    #     return self.get_elements.get_element("duiliejuhekaban", "")