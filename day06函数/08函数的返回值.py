# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\08函数的返回值.py
# 创建日期: 2019.03.06
# 工程目标：return 函数运行后的返回结果 函数传给函数外的值
# 创建作者：binyang
# -*- coding:utf-8 -*-

def mysum(a, b):
    #result = a + b
    he = a + b
    cha = a - b
    #tuple1 = ( )
    #tuple1[0] = he
    #tuple1[1] = cha
    # return tupl
    return (he, cha)    # 没有返回值的时候是无法得到函数的运行结果的且只返回一个整体值 且，return后的语句不再执行    
    print("nihao")

h, c = mysum(1, 2)
#print(tuple1)
print(h, c) 