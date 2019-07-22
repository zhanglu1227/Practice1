
# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]

li = [[1,2],[3,4],[5,6]]

li1 = []

for i in li:
    for j in i:
        li1.append(j)

print(li1)