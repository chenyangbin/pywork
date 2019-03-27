# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\09偏函数.py
# 创建日期: 2019.03.06
# 工程目标：偏函数的使用 函数传入参数的时候大多数的情况下都是一些固定值，
# 为了简化使用，固定某个参数为固定值，而制定的由原函数新定义的函数,某个参数的偏爱值的函数
# 创建作者：binyang
# -*- coding:utf-8 -*-

import functools   #函数工具包
def test1(a, b, c, d=1):
    print("原函数",a + b + c + d)
    #print("原函数")

test1(1, 2, 3)

def test2(a, b, c, d=2):
    print("手动偏函数",a + b + c + d)
    #print("偏函数")

test2(1, 2, 3)

# 使用函数工具对函数的偏爱值进行设定

test3 = functools.partial(test1, d=5)

test3(1, 2, 3)
print("functools设定函数的偏爱值", test3)

