#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:06:18 2019

@author: root
"""

from scapy.all import sniff


doubler = lambda x: x * 2
type(doubler)
doubler(10)
for i in range(0,5):
    print(doubler(i))

#%%
sniff(count=10, prn=lambda packet: packet.show())
    
mailsniff = sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",
                 offline="Downloads/POP.pcap",
                 store=True)
len(mailsniff)
mailsniff[0].show()
mailsniff[0]["IP"].show()
mailsniff[0]["TCP"].show()
mailsniff[4]["TCP"].payload
#%%

def print_credentials(packet):
    if "SSN" in str(packet.payload):
        print(packet.payload)
        print (" ")
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",
                 offline="Downloads/SMTP.pcap",
		    store=False,
		    prn=print_credentials)
