# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 18:37:09 2015

@author: Angie
"""

#-*- coding: utf-8 -*-
#coding:utf-8


#!/usr/bin/python
# Filename: using_file.py

Feature=[1, 1, 1, 1, 1, 1, 3.5, 3.5, 1100, 95, 5, 2]
Result=[1]

f = open('poem.txt', 'a+') # open for 'w'riting
f.write(str(Feature)) # write text to file
f.write(str(Result)) # write text to file
f.write('\n')
f.close() # close the file



