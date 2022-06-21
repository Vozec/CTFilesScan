from utils.misc import execmd
from os import path
import os

def help():
	config = {
		'type':{'traffic':['.pcap']},
		'linux':True,
		'windows':False,
		'name':'Chaosreader'
	}
	return config


def scan(config):
	config_current = help()

	path1 		= '%s/Chaosreader'%config['env_dir']
	path1_save	= '%s/Chaosreader.zip'%config['env_dir']

	if(not path.exists(path1)):
		os.mkdir(path1)

	cmd1  = 'cd %s;'%path1
	cmd1 += 'chaosreader %s;'%config['path']
	cmd1 += 'zip -q -r %s %s;'%(path1_save,path1)
	cmd1 += 'rm -r %s'%path1

	execmd(cmd1)

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