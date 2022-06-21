from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.jpg','.jpeg','.wav','.bmp','.au']},
		'linux':True,
		'windows':False,
		'name':'StegSeek'
	}
	return config


def scan(config):
	config_current = help()
	rockyou = '/usr/share/wordlists/rockyou.txt'
	if(path.exists(rockyou)):

		path1 		 = '%s/stegseek_brute.txt'%config['env_dir']
		path2 		 = '%s/stegseek_seed.txt'%config['env_dir']

		cmd1 = 'stegseek --crack -sf %s -wl %s -f -v -xf /tmp/output_stegseek.txt 2> %s'%(config['path'],rockyou,path1)
		cmd2 = 'stegseek --seed -sf %s -f 2> %s'%(config['path'],path2)

		execmd(cmd1)
		execmd(cmd2)

		result_path = [p for p in (path1,path2) if path.exists(p)]

		return {"type":"file","path":result_path,"content":""}

	else:
		return {"type":"text","path":"","content":"rockyou.txt not found : %s"%rockyou}



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