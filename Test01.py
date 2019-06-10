
# 1、一行代码实现1--100之和，利用sum()函数求和
a = sum(range(1, 101))
print('第1题',a)

# 2、如何在一个函数内部修改全局变量 利用global 修改全局变量
a = 1
def add():
    global a
    a = a + 1
    print('第2题',a)
add()

# 3、列出5个python标准库
# 答：os、unittest、requests、xlrd、xlutlsi

# 4、字典如何删除键和合并两个字典 del和update方法
dic1 = {'a':3, 'b':'19', 'c':'aaa'}
dic2 = {'d':'123','f':'xiaoming'}
# 删除
del(dic1['a'])
print('第4题01',dic1)
# 合并
dic3 = {}
dic3.update(dic1)
dic3.update(dic2)
print('第4题02',dic3)

# 5、谈下python的GIL
# 答：GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），
# 使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。
# 所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

# 6、python实现列表去重的方法
# 答：set方法

# 7、fun(*args,**kwargs)中的*args,**kwargs什么意思？
# 答：*args是可变参数，**kwargs是关键字参数

# 8、python2和python3的range（100）的区别
# 答：python2中的range返回的是一个列表，python3中的range返回的是一个迭代值

# 9、一句话解释什么样的语言能够用装饰器?
# 答：函数可以作为参数传递的语言，可以使用装饰器

# 10、python内建数据类型有哪些？
# 答：整型--int、布尔型--bool、字符串--str、列表--list、元组--tuple、字典--dict

# 11、简述面向对象中__new__和__init__区别
# 答：__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
# __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法
# __init__有一个参数self，就是这个__new__返回的实例
# __new__必须要有返回值，返回实例化出来的实例

# 12、简述with方法打开处理文件帮我我们做了什么？
# 答：打开文件在进行读写的时候可能会出现一些异常状况，常规的f.open写，我们需要try,excpet,finally做异常判断，
# 并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中的f.close()

# 13、列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]

# 14、python中生成随机整数、随机小数、0--1之间小数方法
# 答：随机整数：random.randint(a,b)  区间整数
# 随机小数：用numpy库，利用np.random.randn(5)  生成5个随机小数
# 0-1随机小数：random.random(),注：括号内不传参

# 15、避免转义给字符串加哪个字母表示原始字符串？
# 答：加r

# 16、<div class="nam">中国</div>，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的
# 答：re.findall(pattern, string[, flags])  返回string中所有与pattern相匹配的全部字串，返回形式为数组。
import re
str1 = '<div class="nam">中国</div>'
re1 = re.findall(r'<div class=".*">(.*?)</div>',str1)
print('第16题',re1)

# 17、python中断言方法举例
# 答：assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错
# assertEqual：如两个值相等，则pass
# assertNotEqual：如两个值不相等，则pass
# assertTrue：判断bool值为True，则pass
# assertFalse：判断bool值为False，则Pass

# 20、python2和python3区别？列举5个
# 答：1、python2 print打印不加括号，python3 print打印要加括号
# 2、python2中是raw_input()函数，python3中是input()函数
# 3、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
# 4、python2中unicode表示字符串序列，str表示字节序列
# 5、python2中为正常显示中文，引入coding声明，python3中不需要

# 21、列出python中可变数据类型和不可变数据类型，并简述原理
# 数据类型有：整型，字符串，元组，集合，列表，字典
# 可变数据类型：list、dict、set
# 不可变数据类型：string、int、tuple

# 22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
a = set(s)
print('第22题',sorted(a))

# 23、用lambda函数实现两个数相乘
# 答：Lambda函数，是一个匿名函数，创建语法：lambda 参数:表达式
sum1 = lambda a,b:a*b
print('第23题',sum1(7,8))

# 24、字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

# 25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

# 26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"

# 27、filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 答：filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def fn(a):
    return a % 2 ==1
lis1 = filter(fn,a)
lis1 = [i for i in lis1]
print('第27题',lis1)

# 28、列表推导式求列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str1 = [i for i in a if i%2==1]
print('第28题',str1)

# 29、正则re.complie作用
# 答：re.compile是将正则表达式编译成一个对象，加快速度，并重复使用

# 30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
# 答：a:元祖，b:整数，c:字符串
a = (1,)
b = (1)
c = ('1')
print('第30题',type(a))
print('第30题',type(b))
print('第30题',type(c))

# 31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]
list1 = [1,5,7,9]
list2 = [2,2,6,8]
list1.extend(list2)
print('第31题',list1)
# list3 = list1 + list2
print('第31题',sorted(list1))

# 32、用python删除文件和用linux命令删除文件方法
# 答：python删除文件：os.remove
# linux删除文件：rm

# 33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”

# 36、写一段自定义异常代码
def fn():
    try:
        for i in range(5):
            if i > 2:
                raise Exception('数字大于2')
    except Exception as msg:
        print('第36题',msg)
fn()

# 37、正则表达式匹配中，（.*）和（.*?）匹配区别？

# 39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a = [[1,2],[3,4],[5,6]]
b = [j for i in a for j in i]
print('第39题',b)

# 41、举例说明异常模块中try except else finally的相关意义
# 答：try..except..else没有捕获到异常，执行else语句
# try..except..finally不管是否捕获到异常，都执行finally语句
try:
    a = 'zzz'
    print('第41题',a)
except NameError as msg:
    print('第41题','错误：%s'%msg)
else:
    print('第41题','没有捕获到异常，执行该句')

try:
    a = 'zAz'
    print('第41题',a)
except NameError as msg:
    print('第41题','错误：%s'%msg)
finally:
    print('第41题','不管有没有捕获到异常，都执行该句')


# 42、python中交换两个数值
a,b = 5,6
print('第42题',a,b)
a,b = b,a
print('第42题',a,b)

# 43、举例说明zip（）函数用法

# 44、a="张明 98分"，用re.sub，将98替换为100
# 答：re.sub，实现正则的替换
import re
a="张明 98分"
s = re.sub(r'\d+','100',a)
print('第44题',s)

# 46、a="hello"和b="你好"编码成bytes类型
a="hello"
b="你好"
a = b'hello'
b = '哈哈'.encode()
print('第46题',a,b)
print('第46题',type(a),type(b))

# 47、[1,2,3]+[4,5,6]的结果是多少？
a = [1,2,3]
b = [4,5,6]
print('第47题',a+b)

# 52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
# 53、写一个单列模式
# 54、保留两位小数

# 58、使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
dic = {"name":"zs","age":18}
# del dic["name"]
# print('第58题',dic)
dic.pop("name")
print('第58题',dic)

# 65、IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
# 答：IOError：输入输出异常
# AttributeError：试图访问一个对象没有的属性
# ImportError：无法引入模块或包，基本是路径问题
# IndentationError：语法错误，代码没有正确的对齐
# IndexError：下标索引超出序列边界
# KeyError:试图访问你字典里不存在的键
# SyntaxError:Python代码逻辑语法出错，不能执行
# NameError:使用一个还未赋予对象的变量

# 66、python中copy和deepcopy区别
# 答：浅拷贝只是拷贝了他们最外面的一层，开辟了一个新的地址，如果是嵌套列表那么他指向的还是原来的列表，嵌套列表的内存地址还是一样的
# 深拷贝完完全全复制了一份，重新开辟了一个空间，他的内存地址都和之前的不一样
import copy

a = 'zzz'
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print('第66题',a,id(a))
print('第66题',b,id(b))
print('第66题',c,id(c))
print('第66题',d,id(d))

# 69、请将[i for i in range(3)]改成生成器
# 答：列表表达式的【】改为（）即可变成生成器
a = (i for i in range(3))
print('第69题',type(a))

# 70、a = "  hehheh  ",去除首尾空格
a = "  hehheh  "
print('第70题',a.strip())

# 77、根据键对字典排序（方法一，zip函数）
# 78、根据键对字典排序（方法二,不用zip)
# 82、s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
# 83、正则匹配以163.com结尾的邮箱

# 84、递归求和
def add_sum(num):
    if num >= 1:
        sum1 = num + add_sum(num-1)
    else:
        sum1 = 0

    return sum1

sum1 = add_sum(10)
print('第84题',sum1)

# 85、python字典和json字符串相互转化方法
# 答：dumps是将dict转化成str格式，loads是将str转化成dict格式
import json
dic1 = {'name':'xiaoming','age':22}
# 字典转字符串
str1 = json.dumps(dic1)
print('第85题',str1,type(str1))
# 字符串转字典
dic2 = json.loads(str1)
print('第85题',dic2,type(dic2))

# 87、统计字符串中某字符出现次数
str1 = 'asfdsafsafddderwerkggg'
a = str1.count('a')
print('第87题',a)

# 88、字符串转化大小写
a = 'AAAbbb'
print('第88题',a.upper())
print('第88题',a.lower())

# 89、用两种方法去空格
str1 = 'hello world hello python'
# 方法一
a = str1.replace(' ','')
print('第89题',a)
# 方法二
str2 = str1.split(' ')
b = ''.join(str2)
print('第89题',b)

# 90、正则匹配不是以4和7结尾的手机号
import re
lis1 = ['13478490984','13948790007','10003','13234905545']
for i in lis1:
    ret = re.match('1\d{9}[0-3,5-6,8-9]',i)
    if ret:
        print('第90题','想要的结果',ret.group())
    else:
        print('第90题','%s 不是想要的手机号'%i)

# 97、r、r+、rb、rb+文件打开模式区别
# 答：r:以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# r+：打开一个文件用于读写。文件的指针将会放在文件的开头
# rb:以二进制格式打开一个文件用于只读。文件的指针将会放在文件的开头，这是默认模式

# 99、正则表达式匹配出<html><h1>www.itcast.cn</h1></html>

# 100、python传参数是传值还是传址？
# 答：对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身；
# 而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
# python传参数传址
def addTest(a):
    a += a

a_int = 1
print('第100题',a_int)
addTest(a_int)
print('第100题',a_int)

a_list = [1,2]
print('第100题',a_list)
addTest(a_list)
print('第100题',a_list)





