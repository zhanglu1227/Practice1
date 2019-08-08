
# 将一篇中文文章中的电子邮件地址替换为你自己的电子邮件地址

import re
mystr = '世界你好，lucky168@126.com,你好世界，lucky188@163.com'
print(re.sub(r"\w+@\w+\.\w+",'852827507@qq.com',mystr))