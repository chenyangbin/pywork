# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\17变量作用域的问题.py
# 创建日期: 2019.03.17
# 工程目标：变量在函数中的作用区域
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 变量的作用域
    #1变量的作用域值得是变量的作用范围
    #2python是静态作用域 ， 变量的作用范围取决于它在代码中位置
    
# 命名空间
    #是作用域的体现形式 os.xxx
    #具有不同的操作范围
    # python的命民空间python-LFGB
        # L-LOCAL 函数的命名空间 作用范围，当前的整个函数
        # E-enclos function locals 外部嵌套函数的命名空间，作用范围 闭包函数  
        # G-globa 全局名命空间 作用范围 当前模块文件 声明的全局变量
        # B-builtin 内建模块名命空间 作用范围，所有模块  内建的变量

    #变量的查找顺序 L>E>G>B  由内往外查找
    
