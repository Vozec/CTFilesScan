from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'':[]}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Binwalk'
	}
	return config


def scan(config):
	config_current = help()

	path1 		 = '%s/binwalk.txt'%config['env_dir']
	path_save 	 = '%s/binwalk'%config['env_dir']

	cmd 		 = 'binwalk %s -D=".*" -M --directory=%s > %s;'%(config['path'],path_save,path1)
	cmd 		+= 'zip -q -r %s/binwalk.zip %s ;'%(config['env_dir'],path_save)
	cmd 		+= 'rm -r %s;'%(path_save)

	execmd(cmd)
	
	result_path = [p for p in [path1,path_save] if path.exists(p)]
	
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