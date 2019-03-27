# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\08面向对象补充.py
# 创建日期: 2019.03.21
# 工程目标：面向对象的类，属性，方法 补充
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 类补充
# 创建类对象的类 ，元类创建了类（类也是一种对象）

num = 10
print(num.__class__)  #num 是整型类

str1 = "cmlkaksd"

print(str1.__class__)

print("str的元类", str.__class__)
print("int的元类", int.__class__)

#---------------类的创建方法----------------
#使用元类创建
Dog = type("Dog", (), {"count": 0})
print(Dog)
print(Dog.__dict__)

#---------------元类创建类对象的元类的查找机制 ----------------
#类的创建流程
    #检测对象中是否由明确的__metaclass__属性
    #检测父类中是否有__metaclass__属性
    #检测模块中是否有__meeta__class属性
    #内置的type元类创建该对象


#---------------创建元类----------------


