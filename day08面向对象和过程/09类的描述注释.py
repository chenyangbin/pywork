# 工程目录：c:\Users\bin\OneDrive\share\pywork\day08面向对象和过程\09类的描述注释.py
# 创建日期: 2019.03.21
# 工程目标：类描述，注释文档
# 创建作者：binyang
# -*- coding:utf-8 -*-


#--------------类的描述注释----------------
#描述方式格式

class Person:
    '''
    关于类的描述
    attributes：
        count：人员计数
    '''
    #人的计数
    count = 5


    def run(self, distance, step):
        '''
        run方法功能：
        ；parame distance： 参数的含义，参数的类型，是否有默认值
        ：parameter step：
        ：return：返回值的含义，时间，返回值类型
        '''
        print("类的注释，描述")

help(Person)  #打印源码中的注释

#---------------生成项目文档----------------
#使用内置pydoc模块
    #在工程文件夹下打开cmd端口，而后使用
    #pyhon -m pydoc -k 关键字 查找模块
    #python -m pydoc 模块名  直接打印

#网页查看 cmd # python -m pydoc -p 1234

# 写入文档 # python -m pydoc -w 源码文件名 打印输出html文件

