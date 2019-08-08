'''
有一批网址：

http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415

需要   正则后为：

http://www.interoem.com/ 
http://3995503.com/ 
http://lib.wzmc.edu.cn/ 
http://www.zy-ls.com/ 
http://www.fincm.com/
=
'''

import re
mystr = '''http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415'''

mystr = mystr.splitlines()
print(mystr)

for i in mystr:
    print(re.match(r'http://.*(com/|cn/)',i,re.S).group())
