# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\列表的使用.py
# 创建日期: 2019.02.11
# 工程目标： 列表的使用   the way use  “list” 
# 创建作者：binyang
# -*- coding:utf-8 -*-

# 列表
import random

"""
•序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字- 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

•Python有6个序列的内置类型，但最常见的是列表和元组。即列表、元组、字符串、Unicode字符串、buffer对象和 xrange 对象

•序列都可以进行的操作包括:索引，切片，加，乘，检查成员。

•此外，Python已经内置确定序列的 长度 以及确定 最大大和 最小 的元素的 法。

•列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

•列表的数据项不需要具有相同的类型

•创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
"""
# 示例：：

list_home = ['zhao','qian','sun','li']

list_name = ['周','吴','郑','王']

# python 数据类型抓换
'''
int(x)  将x转换位整数

float(x)    将x转换为浮点数

cpmplex（x）    将x转换为一个复数，其中实数部分为x，虚数部分为0

complex（x，y   将x，y转换到一个复数，其中，x为实数，y为虚数

'''

# 示例
x = 11.023
z = 11
y = 20

print("x11.023转换为整型为：", int(x))

print("z11转换为浮点型为：", float(z))

print("xz结合为虚数为：",complex(x,y))

# 数字运算
'''
Python 数字运算
Python 解释器可以作为一个简单的计算器，您可以在解释器里输入一个表达式，它将输出表达式的值。

表达式的语法很直白： +, -, * 和 /


注意：
在不同的机器上浮点运算的结果可能会不一样。

在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 //

/  除法可以得到含有小数点的精确结果

// 只能得到结果的整数部分

** 可以进行幂运算

变量在使用前必须先"定义"（即赋予变量一个值,确定内存分配地址），否则会出现错误


'''

# 示例 幂运算
print("5的平方：",5 **2)

# 常用的数学函数
'''
数学函数
函数	    返回值 ( 描述 )
abs(x)	    返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	    返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)   如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
exp(x)	    返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	    返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	    如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	    返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	    返回给定参数的最小值，参数可以为序列。
modf(x)	            返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	        x**y 运算后的值。
round(x [,n])	    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	            返回数字x的平方根。
'''

# 随机数函数
'''
随机数函数 
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
Python包含以下常用随机数函数：

此类函数需要通过randon包，静态对象调用来使用  import random     调用random.X()
函数	        描述
choice(seq)	    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	    随机生成下一个实数，它在[0,1)范围内。
seed([x])	    改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。


'''

# 示例随机数函数

print("-----random.X 函数的使用")
list1 = [1,2,3,4,5,6,7,8,9,0]

print("choice  函数随机从序列中选取一个元素：",random.choice(list1))

print("randrang 随机从指定范围输出随机数",random.randrange(1,10,1))

random.shuffle(list1)
print("randon.shuffle 将序列中的元素随机排序",list1)




#  三角函数

'''
三角函数
Python包括以下三角函数：

单独的函数是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法     import math    math.X(x)

注意：x -- -1到1之间的数值。如果x是大于1，会产生一个错误


函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
'''





