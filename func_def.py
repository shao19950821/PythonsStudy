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
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-100))

# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def pop():
    pass
# pass可以用来做占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
age  = 20
if age > 18:
    pass
# 如果不加pass，就会报错

# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# my_abs(1,2)
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
# my_abs('x')
# abs('x')
# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：


# print(my_abs('X'))
print(my_abs(-1))


# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。


