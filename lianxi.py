#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/10/9 16:53
# @Author : jlyu
# @File : lianxi.py

def fucn1(x):
    if x > 1:
        fucn1(x-1)
        print(x)


def fucn2(x):
    if x > 1:
        print(x)
        fucn2(x-1)


alist = [1, "1", 2, "2", 3, "3"]
blist = [e**2 for e in alist if type(e) == int]
clist = []
for f in alist:
    if type(f) == int:
        f *= f
        clist.append(f)

if __name__ == '__main__':
    fucn1(4)
    fucn2(4)
    print(blist)
    print(clist)