# 工程目录：c:\Users\bin\OneDrive\share\pywork\day05-while\02for-遍历集合.py
# 创建日期: 2019.03.05
# 工程目标：for 遍历
# 创建作者：binyang
# -*- coding:utf-8 -*-


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list1:
    print(i, end='  ')
    # break   #直接跳出整个循环
    continue
else:
    print("nihao")
    
# for-elae 使用

# 逆转list
list2 = "你找哦菜单键擦擦从卡卡的长毛"
result = ""
result3 = ""
for k in list2:
    result3 = result3 + k    #加 保持加的位置
    result = k + result      #

print(result)
print(result3)

# 打印设定数值的偶数
setnum = int(input("输入打印范围的数字，只输出偶数"))

for i in range(1, setnum):
    if i % 2 ==0:    # %求模取余符号
        print(i)

    
    






