# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\基本数据类型.py
# 创建日期: 2019.02.11
# 工程目标：数据类型
# 创建作者：binyang
# -*- coding:utf-8 -*-


#多变量赋值

a, b, c = 1, 2.22, 'nihao'



# python数据类型 （序列）
'''
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
Tuple（元组）

List（列表）
Set（集合）
Dictionary（字典）

Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合
'''

# python 数据类型 4大数字类型
# 数字类型包括：int：整型（正负整数，十进制，十六进制...）， float：浮点型（正负小数）， bool：布尔型（真 假 1 0）， complex：复数类型（正负复数）
# type(变量) 用来查询变量类型

# 示例
print("a的类型： ", type(a), a)

print("b的类型： ", type(b), b)

print("c的类型： ",type(c), c)

# python数据类型 字符串 string
# 用'  ' 或者"   " 括起来的字符串
# 字符串索引： 左开头起0，右开头起-1   使用： 变量[头下标:尾下标] 的格式来索引
# 相关用法：   + ：字符串连接符      * ：字符串复制符，后跟复制次数

# 示例
test_str = 'nihao wokeyi baocun'
print(test_str)
print(test_str[0:-1])   # 从头到位输出
print(test_str[2:])     # 从第三个字符开始输出
print(test_str[-2: 0])  #从倒数第二个输出
print(test_str *2)      #复制字符串两次
print(test_str+ "zifu") # 字符串路连接

# 列表
'''
List（列表）
List（列表） 是 Python 中使用最频繁的数据类型。
列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。 
列表截取的语法格式如下：
'''
list = ['abc','786','2.23']
'''
注意：
1、List写在方括号之间，元素用逗号隔开。
2、和字符串一样，list可以被索引和切片。
3、List可以使用+操作符进行拼接。
4、List中的元素是可以改变的。

'''

# 元组
'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。 
元组中的元素类型也可以不相同： 

'''

tuple =('abc','786','2.23')

'''
Tuple（元组）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。 
元组中的元素类型也可以不相同： 

虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。 
构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则： 
string、list 和 tuple 都属于 sequence（序列）
'''

# 集合
'''
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
创建格式：

'''
student = {'tom','jim'}

#字典

'''
字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。 
'''








