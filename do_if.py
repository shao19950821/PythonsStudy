#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: do_if.py

@time: 2018/4/18 12:31

@desc:

'''

# 判断年龄,if条件后要加冒号
age = 20
if age > 18:
    print('age is ',age)
    print('adult')
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
#
# 也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# 注意冒号
#elif 可以做更细的判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# if语句有个执行特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
# if条件还可以简写，比如
x = 0
if x:
    print(True)
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

# 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
# int()传入不合法数字会报错
birth = input('Birth is ')
birth = int(birth)
if birth >= 2000:
    print('00后')
else:
    print('00前')
# 练习
weight = 80.5
height = 1.75
bmi = weight / (height*height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
print(bmi)