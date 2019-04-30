#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:40:17 2019

@author: root
"""

import re
bfor = "BFOR 206 Programming fpr Security Analytics"
re.search(r"bfor",bfor)
re.search(r"BFOR",bfor)

hh_mm = "It is\t13:45"
re.findall(r"\s",hh_mm)
re.split(r"\s",hh_mm)
result=re.search(r"[0-9]{2}:[0-9]{2}",hh_mm)
print(result) 
print(result.group(1))
#re.findalls