from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'other':['.keychain','.keychain-db']},
		'linux':True,
		'windows':False,
		'name':'Keychain'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/Keychain.txt'%config['env_dir']

	if (config['password'] != None):
		res1 = execmd('chainbreaker -f %s -p %s'%(config['path'],config['password'])).decode()
		if(res1 != ""):
			f = open(path1,'w')
			f.write(res1)
			f.close()
		
	result_path = path1 if path.exists(path1) else ''

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