# 工程目录：c:\Users\bin\OneDrive\share\pywork\day03\07OS文件方法.py
# 创建日期: 2019.03.04
# 工程目标：python os.chdir 改变当前工作目录   
# 创建作者：binyang
# -*- coding:utf-8 -*-

#切换当前工作目录为指定路径
'''
os.chdir() 方法用于改变当前工作目录到指定的路径。

语法
chdir()方法语法格式如下：
os.chdir(path)
参数
path -- 要切换到的新路径。

返回值
如果允许访问返回 True , 否则返回False。
'''

import os, sys

retval = os.getcwd()
print("当前的工作目录为：", retval)

# 修改工作目录
'''
path = '/tmp'

os.chdir(path)

retval = os.getcwd()

print("当前的目录修改为“,retval)
'''