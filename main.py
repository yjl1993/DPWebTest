#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/14 17:19
# @Author : jlyu
# @File : main.py

import os

if __name__ == "__main__":
    os.system("pytest -s -q --alluredir report/allure-json")
    os.system("allure generate report/allure-json -o report/allure-report --clean")
