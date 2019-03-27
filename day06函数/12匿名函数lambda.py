# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\12匿名函数lambda.py
# 创建日期: 2019.03.08
# 工程目标：lambda 函数，匿名简单定义函数
# 创建作者：binyang
# -*- coding:utf-8 -*-


#匿名函数，lambda（形参，表达式函数：实参）



l = [{"name": "s1", "age": 19}, {"name": "s2", "age": 16}, {"name": "s1", "age": 20}]

def getkey(x):
    return x["name"]

result = sorted(l, key=getkey)

print(result)

print("你们函数的便捷写法")

result2 = sorted(l, key=lambda x: x["name"])
print(result2)