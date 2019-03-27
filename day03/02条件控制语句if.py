# 工程目录：c:\Users\bin\OneDrive\share\pywork\day03\条件控制语句if.py
# 创建日期: 2019.02.26
# 工程目标：条件控制语句 if
# 创建作者：binyang
# -*- coding:utf-8 -*-


# if 语句
'''
Python中if语句的一般形式如下所示：

if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
如果 "condition_1" 为False，将判断 "condition_2"
如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
如果 "condition_2" 为False，将执行"statement_block_3"块语句
Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。

注意：
1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3、在Python中没有switch – case语句。
以下为if中常用的操作运算符:

操作符	描述
<	    小于
<=	    小于或等于
>	    大于
>=	    大于或等于
==	    等于，比较两个值是否相等
!=	    不等于

下表列出了不同数值类型的 true 和 false 情况：

类型	False	                True
布尔	False(与0等价)	         True(与1等价)
数值	0,   0.0	            非零的数值
字符串	'',  ""(空字符串)	     非空字符串
容器	[],  (),  {},  set()	至少有一个元素的容器对象
None	None	                非None对象

'''