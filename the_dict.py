#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: the_dict.py

@time: 2018/4/18 12:54

@desc: dict学习

'''

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
n = 0
for x in names:
    if(x == 'Tracy'):
        break
    n = n + 1
print(scores[n])
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
#
# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
print(d)
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 99
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d)
# 或是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas',-1))
# 要删除一个key，用pop(key)的方法，对应的value也会从dict删除
print(d)
d.pop('Jack')
print(d)
# dict的key必须是不可变对象，Python中字符串和整数都是不可变的，可以放心的作为key，list是可变的，所以不能作为key
