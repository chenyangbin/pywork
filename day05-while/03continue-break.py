# 工程目录：c:\Users\bin\OneDrive\share\pywork\day05-while\03continue-break.py
# 创建日期: 2019.03.05
# 工程目标：continue - break 的区别
# 创建作者：binyang
# -*- coding:utf-8 -*-


# break 打断 本次循环跳出整个循环
# continue 结束本次循环。继续下次循环

for i in range(1, 100):
    if i == 10:
        #break    # 直接跳出此次循环，不再循环
        continue  # 只跳出符合此次条件的循环，后续的i继续循环
        
    print(i)