# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\11高阶函数的使用场景.py
# 创建日期: 2019.03.07
# 工程目标：高阶函数的使用场景   把一个函数当作另一个函数的参数/返回值
# 创建作者：binyang
# -*- coding:utf-8 -*-

def cacluate(num1, num2, cacluatefunc):
    print(cacluatefunc(num1, num2))
    
def sum(a, b):
    return a + b
    
def jian(a, b):
    return a - b
    
cacluate(4, 5, sum)
cacluate(4,5,jian)


#根据不同参数选择不同功能

def getfunc(flag):
    # 再次定义几个不同功能的函数
    def jia(a, b, c):
        return a + b + c
    
    def chen(a, b, c):
        return a * b * c

    if flag == "+":
        return jia

    if flag == "*":
        return chen

result = getfunc("*")
res = result(1, 2, 3)
print(res)
        



    #2 根据不同的 flag 返回不同的操作函数



    #3 