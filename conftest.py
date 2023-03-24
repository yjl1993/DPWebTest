# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2020/12/22 16:51
# # @Author : jlyu
# # @File : conftest.py.py
#
# import datetime
# import time
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# def get_format_time(extra_info, before=0):
#     try:
#         now_time = datetime.datetime.now()
#         if not before or before == 0:
#             return now_time.strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             if "#" in before:
#                 act_time = before.split("#")[0]
#                 if not act_time:
#                     act_time = 0
#                 accuracy = before.split("#")[1]
#                 if accuracy == "minute":
#                     return (now_time + datetime.timedelta(days=0, minutes=int(act_time))).strftime("%Y-%m-%d %H:%M")
#                 elif accuracy == "hour":
#                     return (now_time + datetime.timedelta(days=0, hours=int(act_time))).strftime("%Y-%m-%d %H")
#                 elif accuracy == "day":
#                     return (now_time + datetime.timedelta(days=int(act_time))).strftime("%Y-%m-%d")
#                 else:
#                     return (now_time + datetime.timedelta(days=int(act_time))).strftime("%Y-%m-%d %H:%M:%S")
#
#             return (now_time + datetime.timedelta(days=int(before))).strftime("%Y-%m-%d %H:%M:%S")
#     except Exception as e:
#         pass
#         #logger.error('get_format_time error:{} '.format(e))
#         return ""
#
#  def get_format_time_range(extra_info, range):
#         try:
#             range_time = range
#             accuracy = 'minute'
#             if '#' in range:
#                 range_time = range.split('#')[0]
#                 accuracy = range.split('#')[1]
#
#             range_start = int(range_time.split('_')[0])
#             range_end = int(range_time.split('_')[1])
#             if range_start > range_end:
#                 pass
#                 #logger.info('get_format_time_range error start after before ')
#                 return ''
#
#             now_time = datetime.datetime.now()
#             if accuracy == 'seconds':
#                 start_time = (
#                     now_time + datetime.timedelta(days=int(range_start))).strftime("%Y-%m-%d %H:%M:%S")
#                 end_time = (
#                     now_time + datetime.timedelta(days=int(range_end))).strftime("%Y-%m-%d %H:%M:%S")
#             elif accuracy == 'minute':
#                 start_time = (
#                     now_time + datetime.timedelta(days=int(range_start))).strftime("%Y-%m-%d %H:%M")
#                 end_time = (
#                     now_time + datetime.timedelta(days=int(range_end))).strftime("%Y-%m-%d %H:%M")
#             elif accuracy == 'hour':
#                 start_time = (
#                     now_time + datetime.timedelta(days=int(range_start))).strftime("%Y-%m-%d %H")
#                 end_time = (
#                     now_time + datetime.timedelta(days=int(range_end))).strftime("%Y-%m-%d %H")
#             elif accuracy == 'day':
#                 start_time = (
#                     now_time + datetime.timedelta(days=int(range_start))).strftime("%Y-%m-%d")
#                 end_time = (
#                     now_time + datetime.timedelta(days=int(range_end))).strftime("%Y-%m-%d")
#             # day不变，hour变
#             elif accuracy == 'dhour':
#                 start_time = (
#                     now_time + datetime.timedelta(days=0, hours=int(range_start))).strftime("%Y-%m-%d %H")
#                 end_time = (
#                     now_time + datetime.timedelta(days=0, hours=int(range_end))).strftime("%Y-%m-%d %H")
#
#             return start_time + ',' + end_time
#         except Exception as e:
#             pass
#             #logger.error('get_format_time_range error:{} '.format(e))
#             return '2022-04-04 11,2022-04-07 11'
#
#
# if __name__ == "__manin__":
#     get_format_time()