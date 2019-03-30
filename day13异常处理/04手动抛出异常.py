# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day13异常处理\04手动抛出异常.py
#创建作者：binyang
#创建目标：手动抛出异常

# 
def set_age(age):

    if age <= 0 or age >= 200:
        raise ValueError("值错误") #返回错误

    else:
        print(age)

try:
    set_age(-10)

except Exception as e:
    print("X",e)