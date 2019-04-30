#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:09:20 2019

@author: root
"""
#%%
import socket
import os
import struct
from ctypes import *

# host to listen on (use ifconfig to find your IP address)
host = "10.0.2.15"

class IP(Structure):
    _fields_ = [
       ("ihl",           c_ubyte, 4),
       ("version",       c_ubyte, 4),
       ("tos",           c_ubyte),
       ("len",           c_ushort),
       ("id",            c_ushort),
       ("offset",        c_ushort),
       ("ttl",           c_ubyte),
       ("protocol_num",  c_ubyte),
       ("sum",           c_ushort),
       ("src",           c_int32),
       ("dst",           c_int32)
       ]
       
    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer=None):
        # map protocol constants to their names
        self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
        # human readable IP addresses
        print("self.src", self.src)
        self.src_address = socket.inet_ntoa(struct.pack("<l",self.src)) 
        self.dst_address = socket.inet_ntoa(struct.pack("<l",self.dst))
        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)
             
class ICMP(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ushort),
        ("unused", c_ushort),
        ("next_hop_mtu", c_ushort)
        ]
    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)
    def __init__(self, socket_buffer):
        pass
  
#file=open('icmpoutput.txt', 'w')    
# this should look familiar from the previous example
if os.name == "nt":
       socket_protocol = socket.IPPROTO_IP
else:
       socket_protocol = socket.IPPROTO_ICMP
       
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
if os.name == "nt":
   sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
try:
    while True:
        # read in a packet
        raw_buffer = sniffer.recvfrom(65535)[0]
        # create an IP header from the first 32 bytes of the buffer
        ip_header = IP(bytes(raw_buffer))
        # print out the protocol that was detected and the hosts
        print("Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.src_address,
                                         ip_header.dst_address))
        # handle CTRL-C
        # if it's ICMP, we want to see the result
        if ip_header.protocol == "ICMP":
            # calculate where our ICMP packet starts
            offset = ip_header.ihl * 4
            buf = raw_buffer[offset:offset + sizeof(ICMP)]
            # create our ICMP structure
            icmp_header = ICMP(buf)
            print("ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.code))
            t="ICMP -> Type: %d Code: %d" % (icmp_header.type, icmp_header.code)
            with open('icmpoutput.txt', 'a') as f:
                f.writelines(ip_header.src_address+' -> '+ip_header.dst_address+'\n'+t+'\n')
        
except KeyboardInterrupt:
    print('Closing Sniffer')
    # if we're using Windows, turn off promiscuous mode
    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

f.close()