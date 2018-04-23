#!/usr/bin/env python

# encoding: utf-8

'''

@author: Qixiang.Shao

@file: func_var.py

@time: 2018/4/23 13:09

@desc: 函数的参数

'''


# 位置参数
# 我们先写一个计算x2的函数
def power(x):
    return x * x


print(power(2))


# 对于power(x)函数，参数x就是一个位置参数。

# 当我们调用power函数时，必须传入有且仅有的一个参数x

# 计算x的n次方函数
def power(x, n):
    result = 1
    while (n > 0):
        result = result * x
        n = n - 1
    return result


print(power(2, 3))


# 默认参数
# 新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：
# print(power(2))
# 报错很明显，power() missing 1 required positional argument: 'n'

# 这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):
    result = 1
    while (n > 0):
        result = result * x
        n = n - 1
    return result


print(power(5))
print(power(5, 3))


# 这样，当我们调用power(5)时，相当于调用power(5, 2)：
# 而对于其他情况，就必须传入n，如power(5,3)

# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 因为将必选参数放在后面，当传入参数的时候，不知道这个参数是代表着取代默认函数，还是必选参数，所以会报错

# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name, gender):
    print('name:', name)
    print('gender', gender)


enroll('Mark', '2')


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Mark', 6)

# 也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，
# 需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

enroll('Adam', 'M', city='Tianjin')


# 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
#
# 先定义一个函数，传入一个list，添加一个END再返回：

def add_end(L=[]):
    L.append('END')
    return L


# 当你正常调用时，结果似乎不错：
print(add_end(['x', 'y', 'z']))
print(add_end(['x', 'y', 'z', 't']))

# 调用默认参数
print(add_end())
print(add_end())
print(add_end())


# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
#
# 原因解释如下：
#
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())
print(add_end())


# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 这样写，调用的时候必须先组装一个list或者元组
print(calc([1, 2, 3]))
print(calc([1, 3, 5, 7]))


# 如果想使用可变参数调用，函数的参数需要变成可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
# 参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(1, 2, 3, 3))
print(calc())

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
num = [1, 2, 3]
print(calc())

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个 含参数名 的参数，这些关键字参数在函数内部自动组装为一个dict。

#定义关键字参数，参数名前加**
def person(name,gender,**kwargs):
    print('name:',name,' gender: ',gender,kwargs)

# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Mark',6)

# 也可以传入任意个 含参数名 的参数
person('Mark',6,city='beijing')
person('Mark',6,city='Beijing',job='student')

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city':'Shanghai','job':'Engineer'}
person('Mark',6,**extra)


# 明明关键字参数

