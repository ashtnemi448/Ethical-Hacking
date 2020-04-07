#!/usr/bin/env python2
'''
import netfilterqueue
import scapy.all as scapy
import os
'''

import subprocess
import sys

def install(package):
    pip.main(['install', package])

def process_packet(packet):

	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.DNSRR):
		qname = scapy_packet[scapy.DNSQR].qname
		print(qname)
		f = open("visited.txt", "a")		
		f.write(qname)
		f.close()

	packet.accept()


try:
    import scapy.all as scapy
except ImportError:
    subprocess.call([sys.executable, "-m", "pip2", "install", 'scapy'])
finally:
    import scapy.all as scapy

try:
    import os
except ImportError:
    subprocess.call([sys.executable, "-m", "pip2", "install", 'os'])
finally:
    import os

try:
    import netfilterqueue
except ImportError:
    subprocess.call([sys.executable, "-m", "pip2", "install", 'netfilterqueue'])
finally:
    import netfilterqueue

try:
    import dropbox
except ImportError:
    subprocess.call([sys.executable, "-m", "pip2", "install", 'dropbox'])
finally:
    import dropbox


os.system("iptables --flush")
os.system("iptables -I INPUT  -j NFQUEUE --queue-num 110")
os.system("iptables -I OUTPUT  -j NFQUEUE --queue-num 110")


queue = netfilterqueue.NetfilterQueue()
queue.bind(110,process_packet)
queue.run()
