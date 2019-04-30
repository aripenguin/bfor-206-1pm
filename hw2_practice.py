#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:59:00 2019

@author: root
"""

import re

#open hacker.log
raw_log=""
time_log=[]
with open('/root/Downloads/hackers.log', 'r+', errors='ignore') as f:
    raw_log = f.readlines()

    
print(raw_log[0:100])
raw_log[0]

for row in raw_log[0:100]:
    #print(row[0:5])
    if re.match(r'---', row[0:5]):
        #print(row)
    elif re.search('[0-9]{2}:[0-9]{2}',row):
        #add to list
        time_log.append(row)
        #time rows.append("data to append)
#print(time_log)
for log in time_log:
    print(log)