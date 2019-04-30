#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:18:25 2019

@author: root
"""

import re

#open hacker.log
raw_log=""
time_log=[]
with open('/root/Downloads/hackers.log', 'r+', errors='ignore') as f:
    raw_log = f.readlines()
    
    
    

#Many users log in and view the chat without commenting. 
    #Which users spent the most time in the logs? (3pts) 
    #Which users logged in the most (2pts)
#Find the most common words (3 pts)
#Count the total number of written messages (only those with actual text content) (2 pts). 
    #Summarize the users that posted the most messages (2pts)
#Find and rank (by count) words not in an English dictionary (3 pts). 
    #This is a simple method that can identify some names of malware tools
#Which hours of the day had the most messages (2pts)? 
    #Which days had the most traffic (or messages) (2pts)?
#Find and list the URLs posted in the chat. (2pts)


#check for logins, and save the username, #of logins [][]
    #extra [] for time online
#Find code online
#use re to find oly messages & count 
    #tabs on who's posts these are
#online
