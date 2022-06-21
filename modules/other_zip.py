from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'other':['.zip']},
		'linux':True,
		'windows':False,
		'name':'ZipCracker'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/zipinfo.txt'%config['env_dir']
	path2 = '%s/hash_zip.txt'%config['env_dir']
	path3 = '%s/zip_cracked.txt'%config['env_dir']

	cmd1 = 'zipinfo %s > %s'%(config['path'],path1)
	cmd2 = 'zipdetails %s >> %s'%(config['path'],path1)

	rockyou = "/usr/share/wordlists/rockyou.txt"
	more = 'timeout 30 john %s --wordlist=%s --show;john %s --show > %s'%(path2,rockyou,path2,path3) if(path.exists(rockyou)) else ''

	cmd3 ="""
if zipdetails %s | grep -q Encryption; then
  zip2john %s > %s;
  %s
fi
"""[1:-1]%(config['path'],config['path'],path2,more)

	[execmd(c) for c in (cmd1,cmd2,cmd3)]
	
	result_path = [p for p in (path1,path2,path3) if  path.exists(p)]
	
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