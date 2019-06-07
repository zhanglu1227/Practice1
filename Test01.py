
# 1、一行代码实现1--100之和，利用sum()函数求和
a = sum(range(1, 101))
print(a)

# 2、如何在一个函数内部修改全局变量 利用global 修改全局变量

# 3、列出5个python标准库
# 答：os、unittest、requests、xlrd、xlutlsi

# 4、字典如何删除键和合并两个字典 del和update方法
dic1 = {'a':3, 'b':'19', 'c':'aaa'}
dic2 = {'d':'123','f':'xiaoming'}
# 删除
del(dic1['a'])
print(dic1)
# 合并
dic3 = {}
dic3.update(dic1)
dic3.update(dic2)
print(dic3)

# 5、谈下python的GIL

# 6、python实现列表去重的方法
# 答：用set

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
# 答：*args是可变参数，**kwargs是关键字参数

# 8、python2和python3的range（100）的区别
# 答：python2中的range返回的是一个列表，python3中的range返回的是一个迭代值

# 9、一句话解释什么样的语言能够用装饰器?

# 10、python内建数据类型有哪些？

# 11、简述面向对象中__new__和__init__区别

# 12、简述with方法打开处理文件帮我我们做了什么？

# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

# 14、python中生成随机整数、随机小数、0--1之间小数方法

# 15、避免转义给字符串加哪个字母表示原始字符串？

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的

# 17、python中断言方法举例

# 20、python2和python3区别？列举5个
# 答：python2 print打印不加括号，python3 print打印要加括号

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 数据类型有：整型，字符串，元组，集合，列表，字典
# 可变数据类型：list、dict、set
# 不可变数据类型：string、int、tuple

# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
a = set(s)
print(sorted(a))

# 23、用lambda函数实现两个数相乘
