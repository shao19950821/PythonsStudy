#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: do_for.py

@time: 2018/4/18 12:35

@desc:python for x in ... 循环

'''

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# for x in 就是把每个元素变量带入x，然后执行缩进块的语句
# 计算 1-10的综合
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
# 如果要计算1-100的和，不可能写1-100，所以Python提供了range(x)可以生成从0到x-1的整数序列，再用list()转换为list
num = range(101)
sum = 0
print(num)
list = list(num)
print(list)
for x in num:
    sum = sum + x
print(sum)