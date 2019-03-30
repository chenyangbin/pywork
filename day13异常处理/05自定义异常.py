# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day13异常处理\05自定义异常.py
#创建作者：binyang
#创建目标：自定义异常的处理方式  

# exception 类所有内置的,系统退出的异常均是从该类派生,应该从该类派生出所有用户的自定义的异常
    #子类


class Lesserror(Exception):
    def __init__(self,msg):
        self.msg = msg
        #print(msg)


def set_age(age):

    if age <= 0 or age >= 200:
        #raise ValueError("值错误") #返回错误
       
        raise Lesserror("错误的")

    else:
        print(age)

try:
    set_age(-10)
    

#抛出错误 方式1

#except Exception as e:
#   print("X",e)




#抛出错误 方式2
except Lesserror as e:
    print("X",e)