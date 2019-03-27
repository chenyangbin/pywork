# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\__pycache__\13内置特殊方法.py
# 创建日期: 2019.03.22
# 工程目标：内置特殊方法 信息格式化，调用操作，索引操作，切片操作，迭代器，描述器
# 创建作者：binyang
# -*- coding:utf-8 -*-


#特殊的内置方法（函数）  内存管理
#内置特殊方法 信息格式化，调用操作，索引操作，切片操作，迭代器，描述器

#---------------信息格式化 __str__  __repr__ ----------------

#自定义参数
#---------------__str__ 描述示实例----------------

class Person:
    def __init__(self, n, a):

        self.name = n  #使用变量参数
        self.age = a

    def __str__(self):  #使用字符串方法返回对应字符串 使用字符串描述示例对象
        return "姓名：%s, 年龄：%s"%(self.name,self.age)
        #return super().__str__()

        #return super().__init__(*args, **kwargs)

p1 = Person("qing", 23)

print(p1.name)
print(p1.age)

print(p1)  #利用__str__ 直接查看p1属性

print(type(p1))

#---------------__repr__ 获取实例本质信息----------------
#使对象具备当作函数被有被调用的能力

class Person1: #类似于偏函数的使用，某个参数偏爱某个值
    def __call__(self, a):
        print(a)
p2 = Person1()
p2("被调用")

class Pen:
    def __init__(self, p_type):
        self.p_type = p_type
        #return super().__init__(*args, **kwargs)

    def __call__(self, p_color):
        print("创建%s类型的笔，是%s颜色" %(self.p_type, p_color))

        pass

bi = Pen("钢笔")
bi("蓝色")
