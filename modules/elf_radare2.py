from utils.misc import execmd
from os import path
import os
import r2pipe

def help():
	config = {
		'type':{'binary':['.bin','.so']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Radare2'
	}
	return config


def rad2(file):
	r = r2pipe.open(file)
	final  = '-'*30+'\n'
	final += r.cmd('aaa;afl')
	final += '-'*30+'\n'
	final += r.cmd("iz")
	final += '-'*30+'\n'
	return final

def rad2_function(file,savepath):
	r = r2pipe.open(file)
	final  = '-'*30+'\n'
	res    = r.cmd('aaa;afl').strip().lstrip().rstrip().split('\n')
	for f in res:
		name = f.split(' ')[-1]
		f = open('%s/%s.txt'%(savepath,name),'w')
		f.write(r.cmd('pdf @%s'%name))
		f.close()


def scan(config):
	config_current = help()

	path1 		 = '%s/Radare2.txt'%config['env_dir']
	path2 		 = '%s/Radare2'%config['env_dir']
	path2_save   = '%s/R2_functions.zip'%config['env_dir']

	if(not path.exists(path2)):
		os.mkdir(path2)

	cnt = rad2(config['path'])
	print(cnt)
	if(cnt != ''):
		f = open(path1,'w')
		f.write(cnt)
		f.close()

	rad2_function(config['path'],path2)
	execmd('zip -q -r %s %s ;rm -r %s'%(path2_save,path2,path2))

	result_path = [p for p in (path1,path2_save) if path.exists(p)]

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