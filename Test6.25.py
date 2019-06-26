
'''
有一个已经排序好的列表，现输入一个数，
要求按原来的规律将它插入数组中
'''

lis = [3, 7, 8, 9, 18, 22, 34]
num = int(input('请输入一个数：'))
# 在列表中加入这个数字
lis.append(num)

# 遍历原列表的数来进行比较大小
for i in range(len(lis)-1):
    if lis[i] >= num:
        for j in range(i, len(lis)):
            lis[j], lis[-1] = lis[-1], lis[j]
            break
print(lis)

# print(sorted(lis, reverse=False))
# print(sorted(reversed(lis)))