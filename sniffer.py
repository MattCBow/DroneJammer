#!/usr/bin/python

from scapy.all import *

ap_list = []
halt = False
def packethandler(pkt) :
	if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 8:
			if pkt.addr2 not in ap_list:
				ap_list.append(pkt.addr2)
				print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)
def stopfilter(pkt):
	return halt

if __name__ == "__main__":
	sniff(iface="wlx00c0ca82925c", prn = packethandler, stop_filter = stopfilter)

