#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: call_func.py

@time: 2018/4/18 22:56

@desc: 调用函数

'''

# abs()，传一个参数，取绝对值
print(abs(-100))

# max()传多个参数，取最大值
print(max(1,2,34,5,666,6))

# int() float() str() bool()数据类型转换
print(int('123'))
print(int(12.34))
print(float(12))
print(str(123))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

# hex()函数把一个整数转换成十六进制表示的字符串：
print(hex(255))