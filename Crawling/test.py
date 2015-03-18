# -*- coding: utf-8 -*-
"""
Created on Sun Mar 01 13:50:34 2015

@author: HengLiu
"""

import urllib2  
  
url = 'http://www.baidu.com/'  
  
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
#values = {'name' : 'WHY',    
#          'location' : 'SDU',    
#          'language' : 'Python' }    
#headers = { 'User-Agent' : user_agent }   
 
req = urllib2.Request(url)    
response = urllib2.urlopen(req)    
the_page = response.read()   
response.close()