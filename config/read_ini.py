#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/18 20:13
# @Author : jlyu
# @File : read_ini.py

import configparser
import os
import ast


class ReadConfig:
    """读取配置文件的方法"""

    # def __init__(self, file_path=None):
    #     if file_path is None:
    #         root_dir = os.path.dirname(os.path.abspath('.'))
    #         config_path = os.path.join(root_dir, "config.ini")
    #     else:
    #         config_path = file_path
    #     self.read_ini = configparser.ConfigParser()
    #     self.read_ini.read(config_path)

    def get_config(self, section, key, file_path=None):
        if file_path is None:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
            config_path = os.path.join(root_path + "/config.ini")
        else:
            config_path = file_path
        self.read_ini = configparser.ConfigParser()
        self.read_ini.read(config_path)
        try:
            value = self.read_ini.get(section, key)
        except BaseException as e:
            print(e)
            value = None
        return value


class ReadElement:
    """读取定位元素的方法"""

    # def __init__(self, file_path=None):
    #     if file_path is None:
    #         root_dir = os.path.dirname(os.path.abspath('.'))
    #         element_path = os.path.join(root_dir, "testdata/elements.ini")
    #     else:
    #         element_path = file_path
    #     self.read_ini = configparser.ConfigParser()
    #     self.read_ini.read(element_path)

    def get_element(self, section, key, file_path=None):
        if file_path is None:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
            element_path = os.path.join(root_path + "/testdata/elements.ini")
        else:
            element_path = file_path
        self.read_ini = configparser.ConfigParser()
        self.read_ini.read(element_path)
        try:
            value = self.read_ini.get(section, key)
        except BaseException as e:
            print(e)
            value = None
        return value


if __name__ == "__main__":
    config = ReadConfig()
    cookies = config.get_config('user_info', 'cookies')
    print(cookies)

#     print(type(cookies))
#     cookies = ast.literal_eval(cookies)
#     for cookie in cookies:
#         cookie_dict = {
#             'name': cookie.get('name'),
#             'value': cookie.get('value'),
#             "expires": "",
#             'path': '/',
#             'httpOnly': False,
#             'HostOnly': False,
#             'Secure': False
#         }
#
#     element = ReadElement()
#     value = element.get_element("baidu", "send_text")
#     print(value)


