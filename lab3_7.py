#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:08:45 2019

@author: root
"""
import socket
#target_host = "google.com"
#target_port = 80

def tcp():
    # create a socket object
    client = socket.socket()

    # connect the client
    client.connect(("0.0.0.0",9999))

    # send some data
    client.send(b"Message to the server!")
            
    # receive some data
    #response = client.recv(1024)
    #(4096)
    #print(response)



def main():
    print("start")
    tcp()

main()

# modify the TCP client so that it connects to the TCP server
# open a new terminal and run the TCP client script
# send the data b”Message to the server!”
# show the terminal output showing the accepted connection
# and the printed message
