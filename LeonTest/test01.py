# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:31:25 2015

@author: Angie
"""

import xdrlib,sys
import xlrd

file= 'file.xlsx'
data = xlrd.open_workbook(file)

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
colnameindex=0
by_index=0
table = data.sheets()[by_index]
nrows = table.nrows #行数
ncols = table.ncols #列数
#colnames =  table.row_values(colnameindex) #某一行数据 
colnames =  ['bache','master','gpa1','gpa2','tofel','gre','paper','sci','school1','school2','school3','admit'] #某一行数据 
list =[]
for rownum in range(0,nrows):
    row = table.row_values(rownum)
    if row:
        app = {}
        for i in range(len(colnames)):
            print i
            app[colnames[i]] = row[i] 
        list.append(app)
print list

a=list[0]['bache']
print a





