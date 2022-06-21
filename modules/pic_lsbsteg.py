from utils.misc import execmd
from os import path
import cv2
from modules.resources.LSBSteg import *

def help():
	config = {
		'type':{'picture':['.png']},
		'linux':True,
		'windows':False,
		'name':'LsbSteg'
	}
	return config

def decode(config):
	im = cv2.imread(config["path"])
	steg = LSBSteg(im)
	return steg.decode_text()

def scan(config):
	config_current = help()

	path1 = '%s/lsbsteg.txt'%config['env_dir']

	data = decode(config)

	if(data != ''):
		f = open(path1,'w')
		f.write(data)
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