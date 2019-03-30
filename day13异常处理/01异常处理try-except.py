# -*- coding:utf-8 -*- 
#创建日期：2019.03.30
#创建路径：c:\Users\bin\OneDrive\share\pywork\day13异常处理\01异常处理.py
#创建作者：binyang
#创建目标：异常处理方法

#--------------------错误--------------------
#逻辑错误
#语法错误


#--------------------异常--------------------
# 语法逻辑正确,出现的未知错误,可以通过其他代码进行处理修复
# 语法异常
# 逻辑异常
#   常见异常
    #除零异常zerodivisionerror,名称异常nameerror,类型异常typeerror,索引异常indexerror,键异常keyerro,值异常valueerror,迭代器异常stopinteration,异常类继承树

#--------------------异常解决--------------------
#系统自动在程序错误的时候会自动触发场景,抛出问题
    #预防处理
        #添加容错code 
        #对数据的输入,数据的处理过程中,提前容错限制
    #手动处理

#--------------------异常捕捉 try except --------------------
# try except 语法
'''
    try:
        可能出现错误的代码

    except:
        要捕捉异常的类型 
        可以书写 多个except 抛出多种异常

    except NameError as ne:
        code

    except 

    else:
        没出现异常的处理
    
    finally:
        出现不出现错误都执行的代码
'''



