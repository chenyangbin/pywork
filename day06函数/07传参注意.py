# 工程目录：c:\Users\bin\OneDrive\share\pywork\day06函数\07传参注意.py
# 创建日期: 2019.03.06
# 工程目标：传参的注意事项
# 创建作者：binyang
# -*- coding:utf-8 -*-


# 值传递： 传入参数的是一个副本，修改副本，对元件没有影响

# 引用传递，* **  通过地址操作同一个元件

# python中只有地址传递，即引用传递 操作的参数为同一个地址空间的参数 如果参数的数据类型是不可改变的，则

def change(num):
    #print(id(num))
    print(num)
    num = 100
    print("传值以后的num的ID",id(num))

    

b = 10
print("b的原始Id",id(b))
change(b)
print("传入函数以后的B的ID", id(b))
#print("函数调用以后的NUM的ID",id(num))