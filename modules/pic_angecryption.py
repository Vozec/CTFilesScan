from utils.misc import execmd
from os import path
from Crypto.Cipher import AES


def help():
	config = {
		'type':{'picture':['.png']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'AngeCryption'
	}
	return config

def Check_param(password,iv):
	if len(password) != 16 or len(iv) != 16:
		return False
	return True

def decode(config):
	password = bytes(config['password'],'utf-8')
	iv		 = bytes(config['iv'])
	try:
		if(Check_param(password,iv)):
			# expected str, bytes or os.PathLike object, not module
			data = open(config['path'], "rb").read()
			cipher = AES.new(password, AES.MODE_CBC, iv)
			return cipher.decrypt(data)
		else:
			return None
	except Exception as ex:
		return None

def scan(config):
	config_current = help()

	path1 = '%s/AngeCryption.data'%config['env_dir']

	result_path = ""

	if(config['password'] != 'password' or config['iv'] != '30'*16 ):
	
		data = decode(config)
		
		if(data != None):
			f = open(path1,'wb')
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