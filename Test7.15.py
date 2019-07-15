#  题目：输入三个整数x,y,z，请把这三个数由小到大输出

li = []

for i in range(3):
    x = int(input("请输入："))
    li.append(x)

li.sort()
print(li)