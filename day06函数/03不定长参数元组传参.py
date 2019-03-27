# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\03不定长参数.py
# 创建日期: 2019.03.05
# 工程目标：不定长参数的使用 形参前加#表示传递元组形参
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 不定长参数的使用：将一个元组或者列表作为形参的集合

def listcount(list1):
    count = list1[0] + list1[1]

    print(type(list1))
    print(count)

listcount((1, 2, 3))  # 不加*时候需要在参数中加括号表示传递元组



def listcount1(*list1):
    count = list1[0] + list1[1]

    print(type(list1))
    print(count)

listcount1(1, 2, 3)  # 加*时候不需要在参数中加括号表示传递元组



