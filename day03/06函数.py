# 工程目录：c:\Users\bin\OneDrive\share\pywork\day03\06函数.py
# 创建日期: 2019.02.27
# 工程目标：函数理解
# 创建作者：binyang
# -*- coding:utf-8 -*-

# 函数
'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
语法
Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体

默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
'''

# 计算面积函数
def area(width, heigh):
    return width * heigh

def print_name(name):
    print("welcome ", name)
    
print_name("严鹏")

print("计算面积函数", area(20, 30))

# 可变类型，不可变类型
'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。


    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，
    不是改变a的值，相当于新生成了a。

    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，
    只是其内部的一部分值被修改了。

python 函数的参数传递：

    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），
    传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，
    只是修改另一个复制的对象，不会影响 a 本身。

    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），
    则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''
# python船体参数的规则
'''
不可便的类型：
    变量的赋值，变量相当于一个指针，不断地指向新的变量值的地址
可变的类型：
    list中，la = [1, 2, 3] la[2] = 5  指的是修改la中的第三个值，la本身并不改变
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

'''

# python传递不可变对象实例
def ChangeInt(a):
    a = 10

b = 2

ChangeInt(b)
print("结果", b)

# 传递可变对象实例
def changeme(mylist):
    mylist.append([1, 2, 3, 4,])
    print("函数内取值", mylist)
    return
mylist=[20, 30]
changeme(mylist)
# 传入函数的和在末尾添加新内容的对象用的是同一个引用。故输出结果如下
print("函数外的取值", mylist)

# 必需参数
'''
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
调用printme()函数，你必须传入一个参数，不然会出现语法错误：
'''
def printme(str1):
    print(str1)
    return
# print(NIHo)会报错 
printme("必须参数nihao")

#关键字参数
'''
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
以下实例在函数 printme() 调用时使用参数名：
'''
def printinfo(name, age):
    print("参数名匹配参数值")
    print("名字", name)
    print("年龄", age)
    return

printinfo(age=20, name="binyang")

# 不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]

加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
'''
def printinfo1(arg1, *vartuple):
    print("----不定长的变量参数-----")
    print(arg1)
    print(vartuple)

printinfo1(70, 80, 50)

# 还有一种就是参数带两个星号 **基本语法如下：
'''
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
加了两个星号 ** 的参数会以字典的形式导入。

'''


