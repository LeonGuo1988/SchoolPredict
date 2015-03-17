# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 13:50:34 2015
@author: HengLiu
"""

import urllib2   
from bs4 import BeautifulSoup
import chardet
import time
import re
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 1. Connect to the web page
url = 'http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=112222'  

#Header
header = {'Host': 'www.1point3acres.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.88',
          'Accept-Encoding': 'gzip, deflate, sdch',
          'Accept-Language': 'en-US,en;q=0.8,zh;q=0.6,zh-CN;q=0.4,zh-TW;q=0.2',
          'Connection': 'keep-alive'} 

#Login info
logininfo = {"username": "guitiantian",
             "password": "794613Ab.",
             }
             
#login to the website
s = requests.Session()
login_res = s.post(url,data=logininfo,headers=header)

#request to connect
main_page = s.get(url).content
#req = urllib2.Request(url)    
#response = urllib2.urlopen(req)
#time.sleep(1) 
#the_page = response.read()  
#response.close()

typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(main_page).get('encoding','utf-8')
the_page = main_page.decode(infoencode,'ignore').encode(typeEncode)
mainsoup = BeautifulSoup(main_page, from_encoding='GB18030')

linkname = []
linkcoll = []
for link in mainsoup.find_all('a',target="_blank"):
    if '/bbs/thread' in link.get('href'):
        linkcoll.append(link.get('href'))
        linkname.append(link.text)

#for url in linkcoll:
#    link_page = s.get(url).content
#    time.sleep(1)
#    infoencode = chardet.detect(link_page).get('encoding','utf-8')
#    link_page = link_page.decode(infoencode,'ignore').encode(typeEncode)
#    soup = BeautifulSoup(link_page, from_encoding='GB18030')
#    print 1
    
link_page = s.get(linkcoll[1]).content
time.sleep(1)
infoencode = chardet.detect(link_page).get('encoding','utf-8')
#link_page = link_page.decode(infoencode,'ignore').encode(typeEncode)
linksoup = BeautifulSoup(link_page, from_encoding='GB2312') 
    
g_data = linksoup.find_all('div',id='ct')

for item in g_data:
    print item.text
    
save = open('text.txt','w')
save.write(str(linksoup.prettify))
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
正则表达式
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
#file.write(the_page)
#file.close()


#reference link
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#http://www.cnpythoner.com/post/310.html
#https://www.youtube.com/watch?v=3xQTJi2tqgk