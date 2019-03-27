# 工程目录：c:\Users\bin\OneDrive\share\pywork\day01\变量.py
# 创建日期: 2019.02.10
# 工程目标：变量的学习
# -*- coding:utf-8 -*-


# 变量：字母，数字，下划线，不能以数字开头
# 区分大小写
# 变量可以改变赋值
# 常量赋值以后，不可变更

'''
name = "nihao"

name2 = name  #name直接指向“nihao”

name = "wiohao"

print(name,name2)

'''

name = input("name:")
print(type(name))  # 查看name的数据输入类型

name2 = int(input("name2:")) # 强制类型转换 无法将str转换为int整形

age = input("age:")

# .format格式化字符串函数的使用
# ''' 是长字符串符号
# %S是占位和符号

# .format 的用法1，使用%s 默认顺序放置
info = '''        
----info----
name:%s   
name2:%s
age:%s
       '''%(name,name2,age)

print(name,age)
print("********")
print(info)

# format的用法2

info2 = '''
-----info2----
    name2:{0}
    age2:{1}
        '''.format(name,age)
print(info2)

