
# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\08字典.py
# 创建日期: 2019.02.16
# 工程目标：字典的使用
# 创建作者：binyang
# -*- coding:utf-8 -*-

# Python3 字典
# 字典是另一种可变容器模型，且可存储任意类型对象。

# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组：
'''
d = {key1: value1, key2:    value2 }
'''

# 创建字典示例
print("-----创建字典-----")
dict1 = {'name': '严鹏', 'age': '23'}
print(dict1)
print("name:",dict1['name'])



# 字典元素的增删改查(键值对)
# 向字典中添加新的键
dict1['职业'] = '大学生'  # 添加键值对
print("添加新的键值后的dict1",dict1)
print("职业",dict1['职业'])

# 删除字典键值对 del dict【】
del dict1['name']
print("删除name键值对后的字典",dict1)

# 字典键的特性

'''
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，(覆盖掉了前一次赋值)

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行(前键后值) 列表可修改

'''

# 字典内置函数&方法
'''
Python字典包含了以下内置函数：

1	len(dict) 计算字典元素个数，即键的总数。

>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> len(dict)

2	str(dict) 输出字典，以可打印的字符串表示。

>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> str(dict)
"{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"


3	type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。	
>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
>>> type(dict)
<class 'dict'>

'''
print("计算字典元素个数len", len(dict1))


print("输出字典字符串格式str", str(dict1))

