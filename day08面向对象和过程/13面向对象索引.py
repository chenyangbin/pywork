# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\13面向对象索引.py
# 创建日期: 2019.03.22
# 工程目标：索引操作
# 创建作者：binyang
# -*- coding:utf-8 -*-


#---------------对实例对象实现类似字典列表的索引操作----------------
# class Person:
#     def __setitem__(self, key, value):
#     def __getitem__():

#     def __delitem__():


#---------------对对象的切片操作----------------
class Person2:
    def __setitem__(self, key, value):
        print(key, value)
        
p3 = Person2()
p3[0:4:2] = [1, 2]


#---------------对实例对象的布尔状态的设定----------------
# __bool__(self)  通过该方法，设定对象的布尔状态

#---------------遍历对象操作----------------
#让自己创建的类可以进行遍历操作 for in
class Person4:
    def __init__(self):
        self.result = 1
        #return super().__init__(*args, **kwargs)

    def __getitem__(self, item):   #使用该方法实现遍历，使用异常抛出
        self.result += 1
        if self.result >= 6:
            raise StopIteration("停止遍历")
        return self.result
    #pass

    def __iter__(self):   #该方法的优先级高于 __getitem__
        print("iter")

    pass

p4 = Person4()

for i in p4:
    print(i)
         

#---------------迭代器的使用·----------------

