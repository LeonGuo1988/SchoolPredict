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
url = 'http://www.1point3acres.com/bbs/thread-115224-1-1.html'  

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
mainsoup = BeautifulSoup(main_page, from_encoding='GB18030')

#%%
# 2. Analyze the web page
names = []
links = []
for item in mainsoup.find_all('a',target="_blank"):
    if 'bbs/thread' in item.get('href'):
        links.append(item.get('href'))
        names.append(item.text)
#%%
n = 0
full_info = []        
for link in links:
    user_name  = names[n]
    link_page = s.get(link).content
    time.sleep(1)
    linksoup = BeautifulSoup(link_page, from_encoding='GB18030') 
    
    #过滤出录取信息和背景信息
    g_data = linksoup.find_all('div',id='ct')
    
    #admission_info = [(item.text).strip().split('[')[-1] for item in admission]    
    #background_info = [(item.text).strip().split(':')[-1] for item in background]
    
    admission = [] #录取信息，如：[15Fall.MS.AD无奖][MIS@U Arizona]通知时间: 2015-03-10
    background = [] #背景信息
    for item in g_data:
        admission = item.find_all('u')
        background = item.find_all('li')

    #term, degree, ad_type, major, school, noti_date
    ad_info = []
    for item in admission:
        ad_info.append(item.text)
    
    ad_info_temp = re.sub('[\[\]@:]','.',ad_info[0])
    ad_info = re.sub(r'\.\.','.',ad_info_temp).split('.')
    del ad_info[0], ad_info[-2]
    
    #录取信息抽取
    ad_term = ad_info[0]
    ad_degree = ad_info[1]
    ad_type = ad_info[2]
    ad_major = ad_info[3]
    ad_school = ad_info[4]
    ad_noti_date = ad_info[5]
    
    #背景信息抽取:
    backgd_info = []
    for item in background:
        backgd_info.append(item.text)
    
    #定位贴链接   
    dingwei_link = backgd_info[0].split(':')[-1] 
    
    #本科信息：学校，专业，GPA
    undergrad = re.sub('[@:]',',',backgd_info[1]).split(',')
    undergrad_major = undergrad[1]   
    undergrad_school = undergrad[2]
    undergrad_GPA = undergrad[3]
    undergrad_comments = undergrad[4] #其他信息
    
    #研究生信息：学校，专业，GPA
    grad = re.sub('[@:]',',',backgd_info[2]).split(',')
    grad_major = grad[1]   
    grad_school = grad[2]
    grad_GPA = grad[3]
    grad_comments = grad[4] #其他信息
    
    #TOEFL & GRE & sub
    toefl = backgd_info[3].split(':')[-1]
    gre = backgd_info[4].split(':')[-1]
    gre_sub = backgd_info[5].split(':')[-1]
    
    #other comment
    other_comment = backgd_info[6].split(':')[-1]
    
    #submition time
    sub_time = backgd_info[7].split(':')[-1]
    
    combine_info = [user_name, link, ad_term, ad_degree, ad_type, ad_major, \
    ad_school, ad_noti_date, dingwei_link, undergrad_major, undergrad_school, \
    undergrad_GPA, undergrad_comments, grad_major, grad_school, grad_GPA, \
    grad_comments, toefl, gre, gre_sub, other_comment, sub_time]
    full_info.append(combine_info)

    n = n + 1
#%%
# 3. Save data
save = open('text.txt','w')
save.write(str(main_page))
save.close
#
save = open('text.txt','w')
for item in full_info:
    for item1 in item:
        save.write("%s ," % item1.encode('GB18030'))
        save.write("\n")   
#
with open('text.txt', 'w') as f:
    for s in full_info[1]:
        f.write((s + u',').encode('unicode-escape'))

with open('text.txt', 'w') as f:
    for s in full_info[1]:
        f.write(str(s).encode('utf-8') + ',')


#file = open('webdata.txt','a')
#line = paper_name + '#' + paper_author + '#' + paper_desc + '#' + citeTimes + '\n'
#file.write(the_page)
#file.close()
#for item in thelist:
#  thefile.write("%s\n" % item)
#
#with open(the_filename, 'w') as f:
#    for s in my_list:
#        f.write((s + u'\n').encode('unicode-escape'))
#reference link
#http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#http://www.cnpythoner.com/post/310.html
#https://www.youtube.com/watch?v=3xQTJi2tqgk