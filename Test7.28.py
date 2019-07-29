# 一个球从100米高度自由下落，每次落地后跳回原高度的一半；再落地，求它在第10次落地时，共经过过少米？第10次反弹多高？

high = 100
meter = 0

for i in range(10):
    if i == 0:   # 第一次落地
        meter += high
        high /= 2
    else:
        meter += (2*high)
        high /= 2

#  print('第%d次落地可以反弹的高度: %f' %((i+1),high))

#  print('第%d次落地经过了%f米' %((i+1),meter))

print('一共经过了%f米'%meter)
print('第10次落地可以反弹的高度: %f米' %high)