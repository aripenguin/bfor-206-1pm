#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:17:41 2019

@author: root
"""
#%%
from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('/root/Downloads/images5.pcap')
print (packets)

# Let's iterate through every packet
for packet in packets:
    # We're only interested packets with a DNS Round Robin layer
    if packet.haslayer(DNSRR):
        # If the an(swer) is a DNSRR, print the name it replied with.
        if isinstance(packet.an, DNSRR):
            print(packet.an.rrname)
print(str(len(packet))+"packet")
            
#https://incognitjoe.github.io/reading-pcap-with-scapy.html
            #%%
from scapy.all import *
import time

def main():

    path = raw_input(/root/Downloads/images5.pcap)
    packs = rdpcap(path)
    option = 0
    while (option != 4):

        print "Options: soon "
        option = input("Enter your option: ")
        i = 0
        count = 0
        if(option == 1):
            print "Number of packets: "
            pack_len = len(packs)
            print pack_len
            print "Sniff tome: "
            print time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(packs[0].time))
            print time.strftime("%Y-%m-%d %H:%M:%S",   time.gmtime(packs[pack_len-1].time))

        elif(option == 2):
            pass # HERE I NEED TO CHECK HOW MANY TCP AND UDP PACKETS I HAVE

        elif(option == 3):
            path = raw_input("Enter new path: ")
            packs = rdpcap(path)

    if __name__ == "__main__":
        main()
