
# 求列表中第二大的元素

lis = [5, 7, 8, 4, 3, 0, 9, 56, 99, 30, 22, 10]
# lis1 = sorted(lis)
# print(lis1)
# print(lis1[-2])

# 思路：已知一列表，对列表进行排序，如果是正序排列，取列表中倒数第二个数的下标，是列表的第二大元素

def elem(lis):
    lis.sort()
    print(lis)
    s = lis[-2]
    print(s)

elem(lis)


