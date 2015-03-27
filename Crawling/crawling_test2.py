# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:55:34 2015

@author: LeonGuo
"""

from bs4 import BeautifulSoup
import time
import re
import requests
import sys
import html5lib

reload(sys)
sys.setdefaultencoding('utf-8')
import pymysql


# 1. Connect to the head web page
headurl = 'http://www.1point3acres.com/bbs/forum-177-1.html'  
heads = requests.Session()
headmain_page = heads.get(headurl).content
headmainsoup = BeautifulSoup(headmain_page,"html5lib")

# 2. Analyze the web page
headmainsoup2 = headmainsoup.find_all('div',{'id':'forum_rules_177'})
for item in headmainsoup2:
    headleonitem = item.find_all('a',{'target':"_blank"})

headlinks = []   
for item in headleonitem:
    if 'bbs/thread' in item.get('href'):
        headlinks.append(item.get('href'))

print headlinks[1]

for headlink in headlinks[12:15]:
    
    url = headlink
    s = requests.Session()
    main_page = s.get(url).content
    mainsoup = BeautifulSoup(main_page,"html5lib")  
    
    # 2. Analyze the web page
    names = []
    links = []
    for item in mainsoup.find_all('a',{'target':"_blank"}):
        if 'bbs/thread' in item.get('href'):
            links.append(item.get('href'))
            names.append(item.text)

    n = 0
    full_info = []   
    for link in links:
        conn = pymysql.connect(host="localhost",user="root",passwd="19880902",db="mytest", charset='utf8')
        cur = conn.cursor()
        time.sleep(5)
        user_name  = names[n]
        link_page = s.get(link).content
        
        linksoup = BeautifulSoup(link_page, from_encoding='GB18030') 
        
        g_data = linksoup.find_all('div',{'class':'pct'})
        
        admission = [] #录取信息，如：[15Fall.MS.AD无奖][MIS@U Arizona]通知时间: 2015-03-10
        background = [] #背景信息
        i=0
        try:   
            for item in g_data:
                if item.find_all('u')==[]:
                    pass  
                else:
                    admission = item.find_all('u')
                    background = item.find_all('li')
        
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
    
            sql="insert ignore into school (user_name,link,ad_term, ad_degree, ad_type,ad_major,\
            ad_school, ad_noti_date, dingwei_link, undergrad_major,undergrad_school,\
            undergrad_GPA, undergrad_comments, grad_major, grad_school, grad_GPA, grad_comments,\
            toefl, gre, gre_sub, other_comment, sub_time) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
            param=(user_name, link, ad_term, ad_degree, ad_type, ad_major, \
            ad_school, ad_noti_date, dingwei_link, undergrad_major, undergrad_school, \
            undergrad_GPA, undergrad_comments, grad_major, grad_school, grad_GPA, \
            grad_comments, toefl, gre, gre_sub, other_comment, sub_time)
        
            cur.execute(sql,param)
            n = n + 1    
            conn.commit()
            cur.close()
            conn.close()   
        except:
            pass
        
        
