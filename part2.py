#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:20:23 2019

@author: root
"""

from scapy.all import *
import requests
import logging

import pyx
#from matlib
import sys
import array as arr

doubler = lambda x: x * 2
type(doubler)
doubler(10)
for i in range(0,5):
    print(doubler(i))

#%%
#iterate through each session & packets
f= open("/root/Downloads/images5.pcap", "r")
packets= rdpcap("/root/Downloads/images5.pcap")
pcap_file="/root/Downloads/images5.pcap"
def http_assembler(pcap_file):
    carved_images=0
    faces_detected=0
    a=rdpcap(pcap_file)
    sessions=a.sessions()
    for session in sessions:
        http_payload=""
        for packet in sessions[session]:
            try:
                if packet[TC].dport==80 or packet[TCP].sport==80:
                    #reassemble the stream
                    http_payload += str(packet[TCP].payload)
            except:
                pass
        headers=get_http_headers(http_payload)
        if headers is None:
            continue
        
    
    
    
    
    
#packets=mailsniff
for packet in packets:
    http_header(packet)
    
    
def http_header(packet):
    http_packet=str(packet)
    if http_packet.find('GET'):
        return GET_print(packet)

def GET_print(packet1):
    ret = "***************************************GET PACKET****************************************************\n"
    ret += "\n".join(packet1.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n"))
    ret += "*****************************************************************************************************\n"
    return ret

sniff(iface='eth0', prn=http_header,offline="Downloads/images5.pcap", filter="tcp port 80")
    
    

    
    r=requests.get('http://')
    try:
        http
    #print (l)
    if 'HTTP' in l:
        print(l)
        #headers = dict(re.findall(b"(?P<name>.*?): (?P<value>.*?)\r\n", headers_raw)
    
    
    
    
        except Exception as e:  
            print(e)   
        #raise # optional, will cause your program to end 
        
    
#%%
#Demonstrate the ability to parse the http headers into a python dictionary object

#%%
#Script can decompress & save image files from the network to your machine

#%%
#Script can recognize faces in images

    