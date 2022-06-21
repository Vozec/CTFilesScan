from utils.misc import execmd
from os import path
import pcapkit

def help():
	config = {
		'type':{'traffic':['.pcap']},
		'linux':True,
		'windows':False,
		'name':'Pcapkit'
	}
	return config

def scan(config):
	config_current = help()

	path1 		 = '%s/Pcapkit.json'%(config['env_dir'])
	plist = pcapkit.extract(fin=config['path'], fout=path1, format='json', store=False)

	result_path = path1 if path.exists(p) else ''

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