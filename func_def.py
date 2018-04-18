#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: func_def.py

@time: 2018/4/18 23:06

@desc: 函数的定义

'''

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#
# 我们以自定义一个求绝对值的my_abs函数为例：
def my_abs (x) :
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-100))
