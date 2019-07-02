
# 求列表中第二大的元素

# lis = [5, 7, 8, 4, 3, 0, 9, 56, 99, 30, 22, 10]
# lis1 = sorted(lis)
# print(lis1)
# print(lis1[-2])

# 思路：已知一列表，对列表进行排序，如果是正序排列，取列表中倒数第二个数的下标，是列表的第二大元素
'''
def elem(lis):
    lis.sort()
    print(lis)
    s = lis[-2]
    print(s)

elem(lis)
'''


# 方法一
'''
设置两个标志位一个存储最大数一个存储次大数
a2存储次大值，a1存储最大值，遍历一次数组即可，先判断是否大于a1，若大于将a1的
值给a2，将lis[i]的值给a1；否则比较是否大于a2，若大于直接将lis[i]的
值给a2；否则pass
'''


def elem(lis):
    a1 = lis[0]
    a2 = lis[0]
    for i in range(1, len(lis)):
        if lis[i] > a1:
            a1 = a2
            a1 = lis[i]
        elif lis[i] > a2:
            a2 = lis[i]
        else:
            pass
    print(a2)

lis = [3, 2, 4, 6, 7, 30, 44, 12, 40]
elem(lis)



# 方法二

def elem1(lis1):
    # 将None赋值给变量 max1,max2
    max1, max2 = None, None
    for i in lis1:
        if max1 is None or i > max1:
            max1, i = i, max1
        elif i is None:
            continue
        if max2 is None or i > max2:
            max2, i = i, max2
        elif i is None:
            continue
    return max2

lis1 = [5, 7, 8, 4, 3, 0, 9, 56, 99, 30, 22, 10]
max2 = elem1(lis1)
print(max2)


