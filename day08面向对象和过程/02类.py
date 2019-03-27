# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\02类.py
# 创建日期: 2019.03.18
# 工程目标：类的创建使用
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 首字母大写 不加括号


#1定义一个类
class Money:  #money是类的名称
    pass

print(Money.__name__)
xxx = Money
print(xxx.__name__)   # money是个变量名称  引用了其定义的类
print(Money)


#根据这个类创建一个对象实例
one = Money()  # 创建实例对象one 在内层中开辟新的空间，创建实例，指向one 类空间和实例空间不是同一个空
               
print(one)

#属性只能通过 对象.xxx  来访问
#变量有对象为宿主，则为属性，否则没有宿主就是个变量

#对象属性的操作，增删改查  (对象是由类实例化而来，进而才能通过对，对象的操作，在对象层面操作属性)
    #增加对象的属性方式
        #1直接通过对象动态添加 语法： 对象.属性 = 值
        #2通过类的初始化构造 _init_方法

# 对象属性操作示例
   
class Person:   #定义一个类
    pass
   
qing = Person()  #根据类创建一个对象

qing.age = 23       #给qing对象增加属性
qing.high = 170
qing.name = "青青子衿"
qing.age = 24  #直接修改属性值 只记录最新只

#del(qing.age)  #删除对象使用del

peng = Person()  #创建对象
peng.age = 26
peng.high = 169
peng.name = "悠悠我心"
del peng.age

print("验证对象属性", qing.age)      #验证属性添加
print("查看全部属性", qing.__dict__)  #查看对象的的全部属性
 #   print(qing.sex)    输出不存在的属性会报错
print("查看属性的类型", type(qing.__dir__()))

# 对象之间不能访问对象之间的属性  在内存中对象的自己区域是独立的 一个类可以生产多个不同的对象
# 具体的实例对象由不同或者相同的属性





# 类的属性和对象的属性 类的一种普遍特点
    #类的属性操作：增删改查
        #增：让对象拥有一些属性
        #删 ：删除一个对象的属性
        #改：修改对象的属性
        #查：访问对象的属性



