# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 13:50:34 2015

@author: HengLiu
"""

import urllib2   
from bs4 import BeautifulSoup
import chardet
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 1. Connect to the web page
#url = 'http://www.1point3acres.com'  
url = 'http://bbs.gter.net/thread-1807984-1-1.html'    
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
#values = {'name' : 'WHY',    
#          'location' : 'SDU',    
#          'language' : 'Python' }    
#headers = { 'User-Agent' : user_agent }   
 
req = urllib2.Request(url)    
#the_page = open('testsourcefile.html','r').read()
response = urllib2.urlopen(req)
the_page = response.read()   
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(the_page).get('encoding','utf-8')
the_page = the_page.decode(infoencode,'ignore').encode(typeEncode)
soup = BeautifulSoup(the_page, from_encoding=infoencode)

save = open('text.txt','w')
save.write(str(soup.prettify))
save.close

'''
soup = BeautifulSoup(the_page)
print soup.prettify()

soup.find_all('a')
for link in soup.find_all('a'):
    print link.text, link.get('href')
    
g_data = soup.find_all('div',class_='pcb')    

for item in g_data:
    print item.text

for item in g_data:
    print item.contents[0].text
    
for item in g_data:
    print item.find_all('li')    
'''

# 2. Analyze the web page
#soup = BeautifulSoup.BeautifulSoup(the_page)

#temp_re = re.match(r'[A-Za-z\s]+(\d*)[A-Za-z\s]+(\d*)', temp_str)

'''
元字符
\b  单词的开头或结尾，也就是单词的分界处   \bhi\b
.   除了换行符以外的任意字符    \bhi\b.*\bLucy\b
*   前边的内容可以连续重复使用任意次数    \bhi\b.*\bLucy\b
\d  匹配一位数字(0，或1，或2，或……)    0\d\d-\d\d\d\d\d\d\d\d
\s  匹配任意的空白符，包括空格，制表符(Tab)，换行符，中文全角空格等
\w  匹配字母或数字或下划线或汉字等。

重复
*	重复零次或更多次
+	重复一次或更多次
?	重复零次或一次
{n}	重复n次
{n,}	重复n次或更多次
{n,m}	重复n到m次
'''



# 3. Save data
#file = open('webdata.txt','a')
#line = paper_name + '#' + paper_author + '#' + paper_desc + '#' + citeTimes + '\n'
# 对象file的write方法将字符串line写入file中
#file.write(the_page)
# 再一次的，做个随手关闭文件的好青年
#file.close()

#http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#http://www.cnpythoner.com/post/310.html
#https://www.youtube.com/watch?v=3xQTJi2tqgk