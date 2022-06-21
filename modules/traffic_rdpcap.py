from utils.misc import execmd
from os import path
import os
from scapy.all import *
from binascii import unhexlify

def help():
	config = {
		'type':{'traffic':['.pcap']},
		'linux':True,
		'windows':False,
		'name':'Rdpcap'
	}
	return config


def scan(config):
	config_current = help()

	path1 	= '%s/RdpCap_Data.data'%config['env_dir']
	path2   = '%s/RdpCap_Data_unhexlify.data'%config['env_dir']
	path3   = '%s/UDP_Data.data'%config['env_dir']

	packets = rdpcap(config['path'])
	all_ = []
	for p in packets:
		try:
			all_.append(p[Raw].load)
		except:
			pass

	###############
	if(all_ != []):
		f = open(path1,'w')
		f.write(str(all_))
		f.close()

		###############
		try:
			all_hex = ''
			for p in all_:
				try:
					all_hex += str(binascii.unhexlify(p))+'\n'
				except:
					pass
			if(all_hex != ''):
				f = open(path2,'w')
				f.write(str(all_hex))
				f.close()
		except:
			pass

	###############
	chunk = b''
	for p in packets:
		if UDP in p:
			try:
				chunk += bytes(p[Raw])+b'\n'
			except:
				pass
	if(chunk != b''):
		f = open(path3,'wb')
		f.write(chunk)
		f.close


	result_path = [p for p in (path1,path2,path3) if path.exists(p)]

	return {"type":"file","path":result_path,"content":""}




#####################
# "config": 
#####################
# env_dir : Directory Created for the scanned filed
# system_tp : linux/windows
# path : File path
# json : Json response required (optional)
# quiet : Use quiet mode ?  (optional)
# password : Password provided (optional)
# iv : Iv provided (hex) (optional)
# formatflag : Format flag (optional)
# module : Module selected (optional)