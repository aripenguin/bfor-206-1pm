#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:20:06 2019

@author: root
"""

import os
os.getcwd()
os.listdir('/root')

file = open('test.txt','r')
contents = file.readlines()
contents
print(contents)
file.close()


with open('test1.txt', 'w') as f:
    f.writelines('new line 2\n')
    
with open('test2.txt', 'a') as f:
    f.writelines('Im with you till the end of the line\n')
    
file=open('test3.txt', 'a')
for i in range(0,10):
    print(i)
    file.writelines(str(i)+'\n')
file.close()
    