'''
定义至少有两个方法的类：

getString：从控制台输入中获取字符串

print string：打印大写的字符串。

还请包含简单的测试函数来测试类方法。
'''

class Test(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input('请输入：')

    def printString(self):
        print(self.s.upper())

a = Test()
a.getString()
a.printString()