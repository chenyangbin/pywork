
# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\13闭包函数的使用.py
# 创建日期: 2019.03.08
# 工程目标：闭包的使用  
# 创建作者：binyang
# -*- coding:utf-8 -*-

# 函数闭包的使用

#函数闭包的条件
'''
闭包函数的使用条件
    1函数定义的时候有嵌套
    2内层函数的引用了外部函数的变量包括参数（内层函数咋运行的时候使用了外部函数的变量）
    3外层函数又把内层的函数 当作返回值进行返回

内层函数加所引用的外层变量称为“闭包”


'''

# 闭包函数的示例

def test():

    a = 10 #条件2 外部函数有变量
    def test2():  #条件一，函数嵌套
        print(a)  #条件2内部函调用了外部函数的变量
    
    return test2()
test()


# 闭包函数的应用场景 根据不同的参数来生成不同的功能的函数
# 参数不同，调用不同的功能

# 闭包函数的功能的示例 根据不同的参数，生成不同的分割线

'''
普通函数调用示例

def creat_line_configer(content, length):
    # 简单功能
    print("-"*(length // 2) + content + "-"*(length // 2))

creat_line_configer("闭包打印线示例", 20)

'''

# 闭包调用示例

def creat_line_configer(content, length):
    # 简单功能
    def line():
        print("-" * (length // 2) + content + "-" * (length // 2))

    return line

# 闭包调用
print("闭包调用内部函数")
line20 = creat_line_configer("闭包调用1", 20)

line40 = creat_line_configer("XXXXX", 40)

print(line20)  # 查看函数的类型
print(line20())
line20()  # 定义了闭包使用的函数以后要调用

line40()


# 闭包函数的使用注意事项 内部嵌套的函数的变量是独立变量 不受外部的变量的干扰
# 如果要修改函数外部的变量 要使用 特殊的关键字 nonlocal 声明是非局部（内部）变量
'''
    1闭包函数的使用中，如果要修改外部的变量的 时候
        1要使用 nonlocal 变量 声明修改的责怪变量是非局部变量（非函数内部使用的变量）
        2否则会被内部函数识别为新定义的变量
        
    2 当函数被调用的时候才会确定使用的变量


'''


def test3():

    num = 10

    def test4():

        # 如果内部函数要使用/修改外部的变量则预定义
        # nonlocal num
        num = 666 # 内部的变量使用了外部变量的名字
        print(num)


    # 测试内部的变量是不是一个新的申请的变量
    print("函数外部的作用域的变量",num)

    test4() # 调用含以后的num
    print("调用函数的num",num)
    return test4()


test3()



