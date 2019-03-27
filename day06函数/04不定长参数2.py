# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\04不定长参数2.py
# 创建日期: 2019.03.05
# 工程目标：不定长传参 形参前加 ** 表示字典传参
# # 创建作者：binyang
# -*- coding:utf-8 -*-

# 加** 使用字典传参，使用的时候像字典一样 函数名（参数名1 =参数1， 参数名2 = 参数2， 。。。。。 ）

def mysun(**kwargs):
    print(kwargs, type(kwargs))


# mysun(1,2,3)   # 注意使用字典传参的时候按照字典的方式 否则报错

mysun(name = "严鹏 ", age = '23') 
