'''
你是一个高级测试工程师，现在要做性能测试，需要你写一个函数，批量生成一些注册使用的账号。
产生的账号是以@163.com结尾，长度由用户输入，产生多少条也由用户输入，用户名不能重复，
用户名必须由大写字母、小写字母、数字组成，
'''
import string
import random

def usname(legth, count):
    f = open('/Users/cola/Desktop/Email.txt', 'w')
    for i in range(count):
        s1 = ''.join(random.sample(string.ascii_lowercase, legth))
        s2 = ''.join(random.sample(string.ascii_uppercase, legth))
        s3 = ''.join(random.sample(string.digits, legth))
        f.write(s1 + s2 + s3 + '@163.com' + '\n')
    f.close()

count = int(input('请输入邮箱的个数，count=').strip())
legth = int(input('请输入邮箱长度，legth=').strip())
usname(legth, count)