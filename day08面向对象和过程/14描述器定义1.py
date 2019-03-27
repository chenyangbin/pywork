# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\14描述器.py
# 创建日期: 2019.03.22
# 工程目标：描述器
# 创建作者：binyang
# -*- coding:utf-8 -*-


#---------------描述器实现对对象的属性访问的控制----------------
#控制对象属性的增改删查 转包通过以下 的描述器的方法实现对属性拦截后的控制
# __set__
# __get__
# __delet__

#---------------描述器的定义----------------
#方式一 @property 由于内部类的方法只能在内中访问，通过装饰器对类中函数的调用访问属性
class Age:
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")
    
    def __deleter__(self, instance):
        print("delet")

class Person:
    # def __init__(self, *args, **kwargs):
    #     self.age = 10
    #    # return super().__init__(*args, **kwargs)

    # @property 这种装饰器的方式也可以实现
    # def get_age(self):
    #     return self.__age


    # def set_age(self, value):
        
    #     if value < 0:
    #         value = 0
    #     self.__age = value

    # def del_age(self):
    #     del self.__age

    #age = property(get_age, set_age, del_age) #手动装饰器  通过类似装饰器的 prooerty类实现 方式访问属性
    age = Age()
    

p = Person()
p.age = 5
print(p.age)
print(type(p.age))

