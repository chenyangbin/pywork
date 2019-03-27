
# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\16递归函数.py
# 创建日期: 2019.03.17
# 工程目标：递归函数，自己调用自己 传递和回归
# 创建作者：binyang
# -*- coding:utf-8 -*-

# 求阶乘   n！ = n * （n-1）！
def jiecheng(n):
    if n == 1:
        return 1
    
    return n * jiecheng(n - 1)

print(jiecheng(4))

# 先逐层传递，而后逐层回归