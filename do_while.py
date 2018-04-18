#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: do_while.py

@time: 2018/4/18 12:42

@desc: Python while 循环

'''

# while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
num = 99
while num > 0:
    sum = sum + num
    num = num - 2
print(sum)
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']
n = 0
for x in L:
    print('Hello , ', x)
# 在循环中，break语句可以提前退出循环。例如，本来要循环打印1～100的数字：
n = 1
while n <= 100:
    print(n)
    n = n + 1
    if n > 10:
        break
print('END')
# 到11的时候退出
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 100:
    n = n + 1
    if n%2 == 0:
        continue
    print(n)
# 要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。
# 大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。