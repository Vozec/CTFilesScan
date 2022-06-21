from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.jpg','.jpeg','.pnm','.ppm']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Outguess'
	}
	return config

def scan(config):
	config_current = help()

	path_extracted = "%s/outguess_extracted.txt"%config['env_dir']

	cmd1 = "outguess -k ''   -r %s %s"%(config['path'],path_extracted)
	cmd2 = "outguess -k '%s' -r %s %s"%(config['password'],config['path'],path_extracted)
	
	for cmd in (cmd1,cmd2):
		res = execmd(cmd)
		if (b'datalen is too long' in res):
			execmd('rm %s'%path_extracted)

	result_path = [p for p in [path_extracted] if path.exists(p)]
	
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