from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.bmp','.png','.gif','.webp','.wav']},
		'linux':True,
		'windows':False,
		'name':'Stegpy'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/stegpy.txt'%config['env_dir']

	cmd = 'stegpy %s > %s'%(config['path'],path1)
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