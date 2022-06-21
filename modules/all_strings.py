from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'':[]}, # All type | All extension
		'linux':True,
		'windows':False,
		'name':'Strings'
	}
	return config


def scan(config):
	config_current = help()	

	path1 = '%s/strings_total.txt'%config['env_dir']
	path2 = '%s/strings_head.txt'%config['env_dir']
	path3 = '%s/strings_bottom.txt'%config['env_dir']

	cmd1 = 'strings -n 7 -t x %s > %s'%(config['path'],path1)
	cmd2 = 'strings -n 7 -t x %s  | head -n 20 > %s'%(config['path'],path2)
	cmd3 = 'strings -n 7 -t x %s  | tail -n 20 > %s'%(config['path'],path3)

	[execmd(x) for x in (cmd1,cmd2,cmd3)]
	
	result_path = [p for p in [path1,path2,path3] if path.exists(p)]
	
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