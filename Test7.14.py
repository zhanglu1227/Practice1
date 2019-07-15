# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列

li = []

for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (y != z) and (z != x):
                li.append([x, y, z])

print(li)