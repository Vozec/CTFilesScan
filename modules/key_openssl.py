from utils.misc import execmd
from os import path
from factordb.factordb import FactorDB

def help():
	config = {
		'type':{'key':['.pem','.pub','.key','.der','.crt']}, #  All extension
		'linux':True,
		'windows':False,
		'name':'Openssl'
	}
	return config


def scan(config):
	config_current = help()

	path1 		 = '%s/Openssl_pubkey.txt'%config['env_dir']
	path2 		 = '%s/Openssl_privkey.txt'%config['env_dir']

	cmd1 = 'openssl rsa -noout -text -inform PEM -in "%s" -pubin -modulus'%(config['path'])
	cmd2 = 'openssl rsa -noout -text -in "%s" -modulus'%(config['path'])

	res1 = execmd(cmd1).decode()
	res2 = execmd(cmd2).decode()

	if("unable to load" not in res1 and res1 != ""):
		try:
			modulus = int(res1.split('Modulus=')[1].strip(),16)
			f = FactorDB(modulus)
			f.connect()
			factors = f.get_factor_list()
			if(len(factors)) != 1:
				res1 += '\n'+'#'*30+'\n'
				res1 += 'Factors Found:\n'
				res1 += str(factors)+"\n"
				res1 += '#'*30
		except Exception as ex:
			pass

		f=open(path1,'w')
		f.write(res1)
		f.close()

	if("unable to load" not in res2 and res2 != ""):
		f=open(path2,'w')
		f.write(res2)
		f.close()

	result_path = [p for p in (path1,path2) if path.exists(p)]

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