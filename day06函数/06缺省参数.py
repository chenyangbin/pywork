# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\06缺省参数.py
# 创建日期: 2019.03.05
# 工程目标：缺省参数。提前对参数的传值进行设定，没有传实参的时候使用默认的设定参数值
# 创建作者：binyang
# -*- coding:utf-8 -*-

def sum(num=0):
    result = num *  num
    print(result)

sum() # 如果不设定缺省参数值，在不传参调用的清空下会报错
sum(5)

