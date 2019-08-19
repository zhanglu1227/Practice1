
# 求s=a+aa+aaa+aaaa+….；其中加几次由键盘输入指定

n = int(input('请输入相加的次数：'))
a = int(input('请输入一个正整数（1-9）：'))
s = 0
m = a
print('s=', end='')
for i in range(1, n+1):
    if i == n:
        print(str(m), end='')
    else:
        print(str(m) + '+', end='')
    s = s + m
    m = m*10+a
print('=' + str(s))
