# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\10字典.py
# 创建日期: 2019.02.26
# 工程目标：字典的操作放啊
# 创建作者：binyang
# -*- coding:utf-8 -*-

'''
序  函数                                                 描述
1	.clear()                                 删除字典内所有元素
2	.copy()                                  返回一个字典的浅复制
3	.fromkeys()                              创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	.get(key, default=None)                  返回指定键的值，如果值不在字典中返回default值
5	key in dict                              如果键在字典dict里返回true，否则返回false
6	.items()                                 以列表返回可遍历的(键, 值) 元组数组
7	.keys()                                  返回一个迭代器，可以使用 list() 来转换为列表
8	.setdefault(key, default=None)和get()    类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	.update(dict2)                           把字典dict2的键/值对更新到dict里
10	.values()                                返回一个迭代器，可以使用 list() 来转换为列表
11	pop(key[,default])                       删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()                                随机返回并删除字典中的一对键和值(一般删除末尾对)。

'''
import copy

# .clear 清空字典
print("-----.clear清空字典-----")
dict1 = {'name': '严鹏', 'age': '23', 'hight': '170cm'}
dict2 = copy.deepcopy(dict1)
dict2.clear()
print("删除字典中的所有元素.clear() %d" % len(dict1), len(dict2))

# fronkeys  创建一个以序列为键，value为初始键值的字典  dict.fromkeys(seq[, value]) 用于预定义字典  value为初始化的键值
print("------fromkeys创建预定义字典-----")
seq = ('name', 'age', 'hight')
dictseqnone = dict.fromkeys(seq)
dictseqvalue = dict.fromkeys(seq, 10)
print("seq无键值预定义字典", dictseqnone)
print("seq预定义初始化键值", dictseqvalue)



# 返回指定的键值 .get

print("返回指定键值.getkey", dict1.get('name'))

# 判断字典中得键是否在字典中 key in dict 在反返回true

print("判断键是否在字典中 key in dict")

if 'name' in dict1:
    print("name在字典中")

# 以列表返回字典中的键值对，元组 .items() 方法以列表返回可遍历的(键, 值) 元组数组。

print("以列表的方式返回字典键值对", dict1.items())

# 返回迭代对象 key 可用list加载
lisr_keys = list(dict1.keys())
print("返回迭代对象.keys() 可任意用list加载", lisr_keys)

# 返回一个迭代器，value 可以list加载
list_value = list(dict1.values())
print("迭代返回键值",list_value)

# 设定默认键值对 dict.setdefault(key, default=None) 如果键不存在于字典中，将会添加键并将值设为默认值。
dict1.setdefault('hobby', None)
print("SETDEFOUT",dict1)

# 字典的叠加， update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
dict3 = {'collor': "蓝色"}
dict4 = {}
dict1.update(dict3)
print(dict1)
print(dict1)


# 删除指定的键值 pop() 返回被删除的键值，如果没有键值，要设置默认值，否则报错返回default
dict1.pop('name')
print("删除指定键值", dict1)

# 随机的删除键值对，并返回键值对
dict1.popitem()
print("随机删除键值对，并返回，如果字典为空，报错keyerror",dict1)
