

# 一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？

# 方法：利用循环去判断x+100和x+268是否为完全平方数

li = []

for i in range(168):
    for n in range(i):
        if i**2 - n**2 == 168:
            x = n**2 - 100
            li.append(x)

print(li)