#-*- coding:utf-8 -*-
print(ord('a'))
print(chr(25991))
a = '\u4e2d\u6587'
print(a)
print('中文'.encode('utf-8'))
print('ABC'.encode('ascii'))
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 如果bytes中包含无法解码的字节，decode()方法会报错,如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'\xe4\xb8\xad\xff\x96\x87'.decode('utf-8',errors='ignore'))
# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
print('Hello %s . My name is %s'%('Michael','Qixiang'))
#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%02d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))
# 练习
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
lastYearGrade = 72
thisYearGrade = 85
percent = (thisYearGrade-lastYearGrade)/lastYearGrade * 100
print("percent is %.1f%%"%percent)
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('percent is {0:.1f}%'.format(percent))
# Python 3的字符串使用Unicode，直接支持多语言。

# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312：
print('中文'.encode('gb2312'))
