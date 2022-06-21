from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.png']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Stegolsb'
	}
	return config


def scan(config):
	config_current = help()

	path1 		 = '%s/StegoLSB_bruteforce.txt'%config['env_dir']
	path2 		 = '%s/StegoLSB_extract.txt'%config['env_dir']

	cmd1 = 'stegolsb bruteforce  %s > %s'%(config['path'],path2)
	cmd2 = 'stegolsb -v extract %s --column-step 2 --rows 1 --cols 128 > %s'%(config['path'],path1)

	execmd(cmd1)
	execmd(cmd2)

	result_path = [p for p in (path1,path2) if path.exists(p)]

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