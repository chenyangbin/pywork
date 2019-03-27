# 工程目录：c:\Users\bin\OneDrive\share\pywork\day05-while\05时间time.py
# 创建日期: 2019.03.05
# 工程目标：time 使用 
# 创建作者：binyang
# -*- coding:utf-8 -*-


import time
'''
result = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())

result2 = time.strftime("%y-%m-%d %H:%M:%S   %A",time.localtime())  # 分隔符号可更改，Y表示4位年，y表示两位年
print(result)
print(result2)

#获取cpu运行时间  time.clock

startime = time.clock()  # 起始时间
'''
for i in range(1,100):
    print(i)
'''

endtime = time.clock()

time = endtime - startime  # 测试一段代码运行的时间差

print(time)
'''

# 休眠n秒
while True:
    result3 = time.strftime("%y-%m-%d %H:%M:%S %A",time.localtime()) 
    print(result3)
    time.sleep(1)
