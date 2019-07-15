#  对一个列表里的数据进行奇偶数分离

num = [3, 4, 5, 79, 20, 24, 18]

li1 = []
li2 = []

while len(num) > 0:
    number = num.pop()
    if number % 2 == 0:
        li1.append(number)
    else:
        li2.append(number)

print(li1)
print(li2)