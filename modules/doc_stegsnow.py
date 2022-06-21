from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'document':['.txt']},
		'linux':True,
		'windows':False,
		'name':'Stegsnow'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/Stegsnow_nopwd.txt'%config['env_dir']
	path2 = '%s/Stegsnow_pwd.txt'%config['env_dir']


	res1 = execmd('stegsnow -C %s'%(config['path'])).decode()
	if(res1 != ""):
		f = open(path1,'w')
		f.write(res1)
		f.close()

	if(config['password'] != None):
		res2 = execmd('stegsnow -C -p "%s" %s'%(config['password'],config['path'])).decode()
		if(res2 != ""):
			f = open(path2,'w')
			f.write(res2)
			f.close()
	

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