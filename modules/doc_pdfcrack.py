from utils.misc import execmd
from os import path
import os

def help():
	config = {
		'type':{'doc':['.pdf']},
		'linux':True,
		'windows':False,
		'name':'PdfCrack'
	}
	return config


def scan(config):
	config_current = help()
	rockyou = "/usr/share/wordlists/rockyou.txt"

	path1 		= '%s/PdfCrack.txt'%config['env_dir']

	if(not path.exists(path1)):
		os.mkdir(path1)

	if('Document is password protected' in execmd("exiftool %s"%config['path']).decode()):
		execmd('pdfcrack --wordlist=%s %s > %s'%(rockyou,config['path'],path1))

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