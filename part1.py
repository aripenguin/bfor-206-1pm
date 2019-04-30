#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:39:47 2019

@author: root
"""

#rom scapy.all import sniff, rdpcap
from scapy.all import *
import pyx
#from matlib

doubler = lambda x: x * 2
type(doubler)
doubler(10)
for i in range(0,5):
    print(doubler(i))

#%%
#sniff(count=10, prn=lambda packet: packet.show())
    
mailsniff = sniff(filter="",
                 offline="Downloads/images5.pcap",
                 store=True)
print("Total packets: ",len(mailsniff))

#mailsniff[0].show()
#mailsniff[0]["IP"].show()
#mailsniff[0]["TCP"].show()
#mailsniff[4]["TCP"].payload
#%%
packets = rdpcap("/root/Downloads/images5.pcap")
#ackets=mailsniff
types=[0,0,0]
for pkt in packets:
    if 'TCP' in pkt:
        #print("TCP")
        types[0]+=1
    if 'UDP' in pkt:
        #print("UDP")
        types[1]+=1
    if 'ICMP' in pkt:
        #print("ICMP")
        types[2]+=1
        
print("# of TCP packets: ",types[0])
print("# of UDP packets: ",types[1])
print("# of ICMP packets: ",types[2])
      
#%%
#build an scapy. Has tool to do this

packets.pdfdump('TrafficFlow.pdf')
#packets.pdfdump(layer_shift=1)



