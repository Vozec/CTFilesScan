from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'binary':['.bin','.so']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Trace'
	}
	return config


def scan(config):
	config_current = help()

	path1 		 = '%s/ltrace.txt'%config['env_dir']
	path2 		 = '%s/strace.txt'%config['env_dir']
	path3 		 = '%s/checksec.txt'%config['env_dir']

	cmd1 = 'timeout 10 echo "guess" | chmod +x %s ;ltrace %s guess2 2> %s'%(config['path'],config['path'],path1)
	cmd2 = 'timeout 10 echo "guess" | chmod +x %s ;strace %s guess2 2> %s'%(config['path'],config['path'],path2)
	cmd3 = 'checksec  %s 2> %s'%(config['path'],path3)

	execmd(cmd1)
	execmd(cmd2)
	execmd(cmd3)

	if(path.exists(path1) and "not an ELF file" in open(path1,'r').read()):
		execmd('rm %s'%path1)

	if(path.exists(path2) and "Exec format error" in open(path2,'r').read()):
		execmd('rm %s'%path2)

	if(path.exists(path3) and "Magic number does not match" in open(path3,'r').read()):
		execmd('rm %s'%path3)


	result_path = [p for p in (path1,path2,path3) if path.exists(p)]

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