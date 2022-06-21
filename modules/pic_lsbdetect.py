from utils.misc import execmd
from os import path

def help():
	config = {
		'type':{'picture':['.png','.jpeg','.jpg']},
		'linux':True,
		'windows':False,
		'name':'LsbDetect'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/LsbDetect.txt'%config['env_dir']
	path_save = "%s/LsbDetect"%config['env_dir']

	cmd = 'mkdir %s;cp %s %s;java -jar modules/resources/StegExpose/StegExpose.jar %s default 0.25 > %s;rm -r %s;rm -r %s/hsperfdata_root'%(path_save,config['path'],path_save,path_save,path1,path_save,config['env_dir'])

	execmd(cmd)
	
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