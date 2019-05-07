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
import sys
import array as arr

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
#packets=mailsniff
types=[0,0,0]
for pkt in packets:
    print (pkt)
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
packets.conversations()


#Show top 5 sessions by # of packets
top=[0,0,0,0,0]
ses=[]
keys=[]
temp=0
changed=0
s=packets.sessions()
#print(s)
for k, v in s.items():#they used iteritems()
    #print(v)
    changed=0
    #print(len(v))
    temp=len(v)
    for i in range(0,5):
        if (temp > top[i]):
            if(changed==0):
                #print("bigger ")
                #print(top[i])
                #print(i)
                
                if((top[i]!=0)==True):
                    #print("NOT 0")
                    #print(top[i])
                    #print(ses[i])
                    ses.pop(i)
                    keys.pop(i)
                ses.insert(i,v)
                keys.insert(i,k)
                top[i]=temp
                #ses.append(v)
                #print(ses)
                changed=1       
print(top)
#print(ses)
#print(keys)
num=0
for s in ses:
    print(ses[num])
    print(keys[num])
    num+=1
#{}


#p=sr1(IP(dst=sys.argv[1]/ICMP))
#if p:p.show()



