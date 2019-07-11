# nums=[2,7,11,15,1,8,7]

# 请找到列表中任意两个元素相加能够等于9的元素集合，列[(2,7), (1,8)]

nums = [2, 7, 11, 15, 1, 8, 7]

li = []

for i in nums:
    for j in nums:
        if i + j == 9:
            a = list((i, j))
            a.sort()
            b = tuple(a)
            if b not in li:
                li.append(b)
print(li)
