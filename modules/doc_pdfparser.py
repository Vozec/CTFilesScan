from utils.misc import execmd
from os import path
import pyUnicodeSteganography as usteg

def help():
	config = {
		'type':{'document':['.pdf']},
		'linux':True,
		'windows':False,
		'name':'PdfParser'
	}
	return config

def scan(config):
	config_current = help()

	path1 		 = '%s/PdfParser.txt'%config['env_dir']
	
	cmd = 'pdf-parser -a %s > %s'%(config['path'],path1)

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