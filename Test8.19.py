'''
制作随机验证码，不区分大小写。
流程：
 - 用户执行程序
 - 给用户显示需要输入的验证码
 - 用户输入的值
'''

import random

def check_code():
    checkcode = ''
    for i in range(4):
        # randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1
        current = random.randrange(0, 4)
        if current != i:
            # random.randint(a,b)用于生成一个指定范围内的整数
            temp = chr(random.randint(65, 90))
        else:
            temp = random.randint(0, 9)
        checkcode += str(temp)
    return checkcode

code = check_code()
print(code)