# 统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]

# 方法一
b = [i for i in a if i > 0]
print(b)

c = [i for i in a if i < 0]
print(c)

# 方法二
m = 0
n = 0
for i in a:
    if i > 0:
        m += 1
    elif i < 0:
        n += 1
    else:
        pass
print(m)
print(n)