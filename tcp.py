#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:02:14 2019

@author: root
"""

import socket
target_host = "google.com"
target_port = 80

# create a socket object
client = socket.socket()

# connect the client
client.connect((target_host,target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
            
# receive some data
response = client.recv(4096)
print(response)
