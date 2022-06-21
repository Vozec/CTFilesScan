import os
from os import path

from utils.misc  import execmd
from utils.logger import logger

def pcapng_to_pcap(filename):
	new_name = filename.split('.pcapng')[0]+'.pcap'
	cmd = "tshark -F pcap -r %s -w %s"%(filename,new_name)
	execmd(cmd)
	return new_name

def cap_to_pcap(filename):
	new_name = filename.split('.cap')[0]+'.pcap'
	cmd = "tshark -F pcap -r %s -w %s"%(filename,new_name)
	execmd(cmd)
	return new_name

def Check_traffic(filename):
	new_name = filename
	if(filename.endswith('.pcapng')):
		new_name = pcapng_to_pcap(filename)
	elif (filename.endswith('.cap')):		
		new_name = cap_to_pcap(filename)


	if(path.exists(new_name)):
		new_name = filename

	return new_name