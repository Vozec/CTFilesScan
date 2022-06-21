from utils.misc import execmd
from os import path
import pyUnicodeSteganography as usteg

def help():
	config = {
		'type':{'document':['.txt']},
		'linux':True,
		'windows':False,
		'name':'Usteg'
	}
	return config

def scan(config):
	config_current = help()

	path1 		 = '%s/Usteg.txt'%config['env_dir']
	
	cnt = usteg.decode(readfile(open(config['path'], "r").read()))
	if(cnt != ""):
		f = open(path1,'w')
		f.write(cnt)
		f.close()
		
	result_path = path1 if path.exists(path1) else ""

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