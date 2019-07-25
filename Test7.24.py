# 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典

l1 = "k:1 |k1:2|k2:3|k3:4"
dic = {}

for i in l1.split('|'):
    key, value = i.split(':')
    dic[key] = value
print(dic)