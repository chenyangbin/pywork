# 工程目录：c:\Users\bin\OneDrive\share\pywork\day05-while\01-while.py
# 创建日期: 2019.03.04
# 工程目标：while-循环 练习无限累加
# 创建作者：binyang
# -*- coding:utf-8 -*-

setnum = int(input("请输入累加值"))
num = 0
result = 0

while num <= setnum:
    num += 1
    result+=num
    print(num)
print(result)
    
