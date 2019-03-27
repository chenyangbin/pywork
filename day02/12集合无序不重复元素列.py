# 工程目录：c:\Users\bin\OneDrive\share\pywork\day02\12集合无序不重复元素列.py
# 创建日期: 2019.02.26
# 工程目标：结合set（）或者 {}
# 创建作者：binyang
# -*- coding:utf-8 -*-

'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：
parame = {value01,value02,...}   或者   set(value)
'''
import copy


parame = {'1', 'b', '你好我在这儿', 'abcdefghijklmb'}

# 添加集合元素操作 .add()
parame.add('nihao')
print("添加元素操作", parame)

# 更新集合元素，可添加列表，元组
parame.update(('1', 'krann'))
print("更新集合元素操作Update ",parame)

#集合内置方法
'''
方法	描述
add()	                为集合添加元素
clear()	                移除集合中的所有元素
copy()	                拷贝一个集合
difference()	        返回多个集合的差集
difference_update()	    移除集合中的元素，该元素在指定的集合也存在。
discard()	            删除集合中指定的元素
intersection()	        返回集合的交集
intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()	        判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	            判断指定集合是否为该方法参数集合的子集。
issuperset()	        判断该方法的参数集合是否为指定集合的子集
pop()	                随机移除元素
remove()	            移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	                返回两个集合的并集
update()	            给集合添加元素
'''

#方法测试
# 添加元素
print("-----添加元素操作------")
parame.add('添加元素')
print("添加元素add（）", parame)

# 清空元素clear
print("------清空元素操作------")
parame2 = copy.deepcopy(parame)
print("深复制操得到parame2作", parame2)
parame2.clear()
print("清空后的parame2", parame2)

# 返回集合的差集，difference（） 即返回一个集合中有但另一个集合中没有的元素
# 返回移除相同元素的新的集合即difference

print("-----返回集合之间的差集-----")
x = {'apple', 'banana', 'cherry'}
y = {'apple','microsoft','google'}
z = y.difference(x)
print("返回YX的差集", z)

# 操作集合，移除两个集合中的相同元素difference_update
print("-----移除两个集合中相同的元素------")
e = copy.deepcopy(x)
f = copy.deepcopy(y)
e.difference_update(f)
print("移除EF集合中的相同同的元素",e)

# 移除指定集合元素 discard
'''
discard() 方法用于移除指定的集合元素。

该方法不同于 remove() 方法，
因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会。
'''
print("-----移除指定元素-----")
x.discard('apple')
print("移除指定元素", x)

# intersrction返回两个集合或的集合中都巴汉的集合，返回交集
'''
描述
intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。

语法
intersection() 方法语法：
set.intersection(set1, set2 ... etc)

参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开

返回值
返回一个新的集合。
'''
print("-----返回多个集合交集-----")
h = {'a', 'b', 'c'}
i = {'a', 'b', 'e'}
l = {'a','b','f'}
k = h.intersection(i,l)
print("返回交集", k)


# 移除多个集合中的不重复的元素
'''
ntersection_update() 方法用于获取两个或更多集合中都重叠的元素，即计算交集。

intersection_update() 方法不同于 intersection() 方法，因为 intersection() 方法是返回一个新的集合，
而 intersection_update() 方法是在原始的集合上移除不重叠的元素。

语法
intersection_update() 方法语法：
set.intersection_update(set1, set2 ... etc)

参数
set1 -- 必需，要查找相同元素的集合
set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开
'''
print("-----移除所操作的集合与其他集合的不重复的元素------")
m = {'a', 'b', 'c'}
n = {'a', 'b', 'e'}
o = {'a','b','f'}
m.intersection_update(n, o)
print("移除操作集合中的不同的元素", m)
print("移除操作集合中的不同的元素对比集合，未操作集合", n)

# isdisjion 判断两个集合是否包含相同的元素
'''
描述
isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。。

语法
isdisjoint() 方法语法：
set.isdisjoint(set)

参数
set -- 必需，要比较的集合

返回值
返回布尔值，如果不包含返回 True，否则返回 False。
'''

print("-----判断两个集合中是否有相同的元素-----")
set1 = {'a', 'b', 'c'}
set2 = {'a', 'b', 'e'}
flag = set1.isdisjoint(set2)
print("判断集合set1和集合set2中是否有相同的元素并返回flag包含返回false",flag)

# 




