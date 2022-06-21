from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'traffic':['.pcap']},
		'linux':True,
		'windows':False,
		'name':'SslDump'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/ssldump.txt'%config['env_dir']

	cmd = 'ssldump -r %s'%(config['path'])

	res = execmd(cmd).decode()

	if(res != ''):
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