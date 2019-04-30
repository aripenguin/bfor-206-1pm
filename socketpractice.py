#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:55:13 2019

@author: root
"""
#%%
import os
import socket

#host ip address 
host="10.0.2.15"
#%%
socket_protocol=socket.IPPROTO_ICMP

sniffer=socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))
#%%
print(sniffer.recvfrom(65565))