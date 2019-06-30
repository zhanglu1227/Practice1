'''
2、编写一个程序来计算给定数字的阶乘。

结果应以逗号分隔的顺序打印在一行上。

假设向程序提供以下输入：8

那么，输出应该是：40320
'''

a = int(input('请输入一个数：'))

def nums(a):
    if a == 0:
        return 1
    else:
        return a * nums(a - 1)

print(nums(a))