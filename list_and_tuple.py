#-*- coding:utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
# 变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1。

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
# 倒数第二个就是-2，倒数第三个就是-3
print(classmates[-2])
print(classmates[-3])
# list是个可变的有序表，所以，可以往list里添加元素
classmates.append('Adam')
print(classmates[3])
# 也可以把元素插入到指定索引的位置
classmates.insert(1,'Jack')
print(classmates)
# 要删除list末尾的元素，用pop方法
print(classmates.pop())
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
print(classmates.pop(1))
print(classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1]='Shao'
print(classmates)
# list里面元素的类型可以不同
L = ['Apple',1,True]
print(L)
# list里面的元素也可是是个list
s=['python','java',['ruby','c++'],'c']
print(len(s))
print(len(s[2]))
# s[2]拿到list['ruby','c++'],s[2][1]拿到'c++'
print(s[2][1])
# 如果一个list里面什么元素都没有，那么这个list的长度为0
L = []
print(len(L))

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# tuple初始化方法是用()，list是用[]
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# 如果要定义一个空的tuple，可以写成()：
t = ()
print(t)
# 但是，要定义一个只有1个元素的tuple，如果你这么定义：
t = (1)
print(t)
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)
# 可变tuple
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# tuple指向没变，变的是tuple里的list