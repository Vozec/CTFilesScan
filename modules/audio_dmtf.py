from utils.misc import execmd
from os import path
import os

def help():
	config = {
		'type':{'audio':['.wav','.mp3']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Dmtf'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/Dmtf.txt'%config['env_dir']

	cmd = 'dtmf -v %s'%(config['path'])
	
	res = execmd(cmd).decode()

	if(res != ""):
		f = open(path1,'w')
		f.write(res)
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