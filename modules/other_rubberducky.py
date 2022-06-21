from utils.misc import execmd
from os import path
from ducktoolkit import decoder

def help():
	config = {
		'type':{'other':['.bin']},
		'linux':True,
		'windows':False,
		'name':'RubberDucky'
	}
	return config


def scan(config):
	config_current = help()

	path1 = '%s/RubberDucky_Decoded.txt'%config['env_dir']

	res1 = decoder.decode_script('gb',open(config['path'],'rb').read())

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