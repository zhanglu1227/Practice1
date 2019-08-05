
# 正则匹配以163.com结尾的邮箱

import re

def main():
    email = input('请输入邮箱：')
    ret = re.match(r'[a-zA-Z0-9]{4,20}@163\.com$',email)
    if ret:
        print('邮箱正确')
        return
    else:
        print('邮箱错误')

if __name__ == '__main__':
    main()


