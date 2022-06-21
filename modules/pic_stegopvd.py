from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.png']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Stegopvd'
	}
	return config


def scan(config):
	config_current = help()
	path1 		 = '%s/lsbdetect.png'%config['env_dir']
	cmd = 'cd %s;cp %s %s;stegolsb stegdetect -i %s -n 2;mv *2LSBs* %s;rm stego_copy.png'%(config['env_dir'],config['path'],'stego_copy.png',config['env_dir']+"/stego_copy.png",path1)
	execmd(cmd)
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