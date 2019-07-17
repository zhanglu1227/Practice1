'''
給定一组水果 ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
随机100次，每次随机选一种水果
使用dic统计水果出现的次数
'''


import random
dic = {}
fruit = ['香蕉', '草莓', '苹果', '梨子', '西瓜', '芒果', '葡萄']
for i in range(100):
    f = random.choice(fruit)
    if f in dic:
        dic[f] += 1
    else:
        dic[f] = 1

print(dic)