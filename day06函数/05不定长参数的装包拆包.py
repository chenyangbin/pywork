# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\05缺省参数.py
# 创建日期: 2019.03.05
# 工程目标：不断长参数的装包和拆包          
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 不定长参数的装包：把传递的参数包装为一个集合（元组或者字典）

# 拆包操作：把集合的参数分解为单个的个体

#  装包传参： 将参数作为整体传入，使用* 或者**在形参前，直接传入参数


def sum(a, b, c, d):
    print(a+b+c+d)

def test(*args):
    print(args)

    # 拆包
    print(*args)

    print("参数的装包")

    sum(*args)  # 参数的装包传参

    print("参数的拆包引用")
    sum(args[0],args[1],args[2],args[3])  #参数的拆包传参 相当于指针的引用

test(1, 2, 3, 4)  #传参的装包


