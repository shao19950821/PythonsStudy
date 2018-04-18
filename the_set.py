#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: the_set.py

@time: 2018/4/18 19:02

@desc: set的学习

'''

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3,4])
print(s)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。
#
# 重复元素在set中自动被过滤：
s = set([1,1,2,3,3,4,4,5,6,6,7])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(8)
print(s)
s.add(8)
print(s)
# 通过remove(key)方法可以删除元素:
s.remove(8)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
a.sort()
print(a)
# 而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
print(a.replace('a','A'))
print(a)
b = a.replace('a','A')
print(b)