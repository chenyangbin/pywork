# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\10高阶函数-嵌套.py
# 创建日期: 2019.03.07
# 工程目标：高阶函数，函数的可以作为其他函数的参数的函数
# 创建作者：binyang
# -*- coding:utf-8 -*-

# sorte 排序函数为例
# sorte（iterable，key，reverse） 排序对象，排序关键字，

# 列表，字典
l = [{"name": "sz1", "age": 18}, {"name": "sz2", "age": 20},
 {"name": "sz3", "age": 17}]

# 找打分类关键字
def getkey(x):
    return x["age"]

result = sorted(l, key=getkey)

print(result)
