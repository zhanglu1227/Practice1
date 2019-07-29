# 遍历列表
li = ['功能测试','自动化测试','安全测试',['性能测试',['脚本开发','压测','性能调优']]]


# 方法一
for x in li:
    if isinstance(x, list):  # 判断每一个元素是否时列表
        for y in x:
            if isinstance(y, list):
                for z in y:
                    print(z)
            else:
                print(y)
    else:
        print(x)


# 方法二
def num(li1):
    for i in li1:
        if isinstance(i, list):
            num(i)

        else:
            print(i)

num(li)